from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, Quiz, Question, Answer, Badge, UserProfile

class BadgeAwardingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = Client()
        self.client.login(username='testuser', password='password123')
        
        self.category = Category.objects.create(name='Test Category')
        self.badge_gold = Badge.objects.create(
            name='Gold Badge', category=self.category, tier='GOLD', min_score=100
        )
        self.badge_silver = Badge.objects.create(
            name='Silver Badge', category=self.category, tier='SILVER', min_score=80
        )
        self.badge_bronze = Badge.objects.create(
            name='Bronze Badge', category=self.category, tier='BRONZE', min_score=60
        )
        
        self.quiz = Quiz.objects.create(title='Test Quiz', category=self.category)
        
        # Create 10 questions
        for i in range(10):
            q = Question.objects.create(quiz=self.quiz, text=f'Q{i}')
            Answer.objects.create(question=q, text='Correct', is_correct=True)
            Answer.objects.create(question=q, text='Wrong', is_correct=False)

    def test_award_bronze_badge(self):
        """Test awarding only bronze for 60% score."""
        # Setup session to simulate active quiz (required by the view)
        session = self.client.session
        question_ids = [q.id for q in self.quiz.questions.all()]
        session[f'quiz_active_questions_{self.quiz.id}'] = question_ids
        session.save()
        
        # Answer 6 correct, 4 wrong
        post_data = {}
        questions = self.quiz.questions.all()
        for i, q in enumerate(questions):
            ans = q.answers.filter(is_correct=(i < 6)).first()
            post_data[f'question_{q.id}'] = ans.id
            
        response = self.client.post(reverse('quiz_take', args=[self.quiz.slug]), post_data)
        
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.badges.count(), 1)
        self.assertIn(self.badge_bronze, profile.badges.all())

    def test_award_gold_all_badges(self):
        """Test awarding all badges for 100% score."""
        session = self.client.session
        question_ids = [q.id for q in self.quiz.questions.all()]
        session[f'quiz_active_questions_{self.quiz.id}'] = question_ids
        session.save()
        
        # Answer all correct
        post_data = {}
        for q in self.quiz.questions.all():
            ans = q.answers.filter(is_correct=True).first()
            post_data[f'question_{q.id}'] = ans.id
            
        self.client.post(reverse('quiz_take', args=[self.quiz.slug]), post_data)
        
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.badges.count(), 3)
        self.assertIn(self.badge_gold, profile.badges.all())
        self.assertIn(self.badge_silver, profile.badges.all())
        self.assertIn(self.badge_bronze, profile.badges.all())
