import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .models import Quiz, Question, Answer, QuizAttempt, Badge, UserProfile

def landing_page(request):
    return render(request, 'quiz/landing_page.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'quiz/register.html', {'form': form})

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

@login_required
def dashboard(request):
    attempts = QuizAttempt.objects.filter(user=request.user)
    
    # Decorate attempts with percentage for the template
    decorated_attempts = []
    for attempt in attempts:
        percent = (attempt.score / attempt.total_questions * 100) if attempt.total_questions > 0 else 0
        decorated_attempts.append({
            'quiz': attempt.quiz,
            'score': attempt.score,
            'total_questions': attempt.total_questions,
            'timestamp': attempt.timestamp,
            'percent': percent
        })

    total_attempts = attempts.count()
    if total_attempts > 0:
        avg_score = sum([a.score / a.total_questions for a in attempts if a.total_questions > 0]) / total_attempts * 100
    else:
        avg_score = 0
        
    return render(request, 'quiz/dashboard.html', {
        'attempts': decorated_attempts,
        'total_attempts': total_attempts,
        'avg_score': avg_score
    })

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    badges = user_profile.badges.all()
    earned_badge_ids = list(badges.values_list('id', flat=True))
    all_badges = Badge.objects.select_related('category').order_by('category__name', 'min_score')
    
    attempts = QuizAttempt.objects.filter(user=request.user)
    total_attempts = attempts.count()
    if total_attempts > 0:
        avg_score = sum([(a.score / a.total_questions) for a in attempts if a.total_questions > 0]) / total_attempts * 100
    else:
        avg_score = 0
        
    return render(request, 'quiz/profile.html', {
        'profile': user_profile,
        'badges': badges,
        'earned_badge_ids': earned_badge_ids,
        'all_badges': all_badges,
        'total_attempts': total_attempts,
        'avg_score': avg_score
    })

@login_required
def quiz_take(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    
    if request.method == 'POST':
        # Retrieve the specific questions asked in this attempt from the session
        question_ids = request.session.get(f'quiz_active_questions_{quiz.id}')
        if not question_ids:
            return redirect('quiz_take', quiz_slug=quiz_slug)
            
        questions = Question.objects.filter(id__in=question_ids)
        score = 0
        total = questions.count()
        selections = {}
        
        for question in questions:
            answer_id = request.POST.get(f'question_{question.id}')
            if answer_id:
                selections[str(question.id)] = int(answer_id)
                try:
                    answer = Answer.objects.get(id=answer_id)
                    if answer.is_correct:
                        score += 1
                except Answer.DoesNotExist:
                    pass
        
        # Save attempt
        QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total_questions=total
        )
        
        # Award badges based on score
        if total > 0:
            score_percent = (score / total) * 100
            user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
            eligible_badges = quiz.category.badges.filter(min_score__lte=score_percent)
            if eligible_badges.exists():
                user_profile.badges.add(*eligible_badges)
                
        
        # Track recently seen questions to avoid repetition in next attempt
        recently_seen = request.session.get(f'recently_seen_{quiz.id}', [])
        recently_seen.extend(question_ids)
        # Keep only the last 50 seen questions
        request.session[f'recently_seen_{quiz.id}'] = recently_seen[-50:]
        
        request.session[f'quiz_score_{quiz.id}'] = score
        request.session[f'quiz_total_{quiz.id}'] = total
        request.session[f'quiz_selections_{quiz.id}'] = selections
        # We keep the active questions in session for the result page to show the breakdown
        return redirect('quiz_result', quiz_slug=quiz.slug)
    
    else:
        # GET request: Pick 10 random questions
        all_questions = list(quiz.questions.all())
        recently_seen = request.session.get(f'recently_seen_{quiz.id}', [])
        
        # Prioritize questions not recently seen
        new_questions = [q for q in all_questions if q.id not in recently_seen]
        seen_questions = [q for q in all_questions if q.id in recently_seen]
        
        random.shuffle(new_questions)
        random.shuffle(seen_questions)
        
        # Combine them, new ones first
        sampled_questions = new_questions + seen_questions
        
        # Prepare questions with shuffled answers
        questions_with_answers = []
        for q in sampled_questions:
            answers = list(q.answers.all())
            random.shuffle(answers)
            questions_with_answers.append({
                'id': q.id,
                'text': q.text,
                'shuffled_answers': answers
            })
            
        # Store the IDs in the session to ensure POST handles the SAME questions
        request.session[f'quiz_active_questions_{quiz.id}'] = [q['id'] for q in questions_with_answers]
        
        return render(request, 'quiz/quiz_take.html', {
            'quiz': quiz,
            'questions': questions_with_answers
        })

@login_required
def quiz_result(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    score = request.session.get(f'quiz_score_{quiz.id}', 0)
    total = request.session.get(f'quiz_total_{quiz.id}', 0)
    selections = request.session.get(f'quiz_selections_{quiz.id}', {})
    question_ids = request.session.get(f'quiz_active_questions_{quiz.id}', [])
    
    percentage = (score / total * 100) if total > 0 else 0
    # Circumference for r=80 is 2 * pi * 80 = 502.65
    percentage_offset = 502.65 * (1 - percentage / 100)
    
    # Prepare breakdown based on the specific questions asked
    breakdown = []
    questions = Question.objects.filter(id__in=question_ids)
    
    # Maintain the same order as seen in the quiz if possible, 
    # but here we just iterate through the questions we found
    for question in questions:
        selected_answer_id = selections.get(str(question.id))
        selected_answer = None
        if selected_answer_id:
            try:
                selected_answer = Answer.objects.get(id=selected_answer_id)
            except Answer.DoesNotExist:
                pass
        
        correct_answer = question.answers.filter(is_correct=True).first()
        
        breakdown.append({
            'question': question.text,
            'selected_answer': selected_answer.text if selected_answer else "None",
            'correct_answer': correct_answer.text if correct_answer else "None",
            'is_correct': selected_answer.is_correct if selected_answer else False
        })
    
    return render(request, 'quiz/quiz_result.html', {
        'quiz': quiz,
        'score': score,
        'total': total,
        'percentage': percentage,
        'percentage_offset': percentage_offset,
        'breakdown': breakdown
    })
