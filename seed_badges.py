import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz.models import Category, Badge

def create_initial_badges():
    badge_data = {
        'Python Basics': ('Python Pioneer', 'Mastered the fundamentals of Python programming.', '🐍'),
        'Django Views': ('View Virtuoso', 'Perfectly understood Django class and function-based views.', '🎯'),
        'React Fundamentals': ('React Ranger', 'Conquered the core concepts of React.', '⚛️'),
        'Physics': ('Newton\'s Heir', 'Demonstrated total mastery over physical principles.', '🍎'),
        'Chemistry': ('Alchemist Prime', 'Achieved a perfect reaction in Chemistry knowledge.', '🧪'),
        'Machine Learning': ('Data Overlord', 'Trained your brain to 100% accuracy in ML.', '🤖'),
        'GATE': ('GATE Keeper', 'Unlocked top potential in GATE concepts.', '🗝️'),
        'Basic Grammar': ('Grammar Guru', 'Perfectly articulated the rules of Basic Grammar.', '✍️'),
        'History': ('Time Traveler', 'Achieved perfect recall of historical events.', '⏳'),
        'Geography': ('Global Navigator', 'Mastered the map with 100% geographical accuracy.', '🌍'),
        'Political Science': ('Diplomat Prime', 'Fully understood political systems and structures.', '🏛️'),
        'Reasoning': ('Logic Luminary', 'Demonstrated flawless logical reasoning.', '🧩'),
    }

    categories = Category.objects.all()
    created_count = 0

    for category in categories:
        if category.name in badge_data:
            name, desc, icon = badge_data[category.name]
            badge, created = Badge.objects.get_or_create(
                category=category,
                defaults={'name': name, 'description': desc, 'icon': icon}
            )
            if created:
                print(f"Created badge '{name}' for category '{category.name}'")
                created_count += 1
        else:
            # Fallback for dynamic/unlisted categories
            badge, created = Badge.objects.get_or_create(
                category=category,
                defaults={
                    'name': f"{category.name} Master", 
                    'description': f"Achieved a perfect score in {category.name}.", 
                    'icon': '🏅'
                }
            )
            if created:
                print(f"Created default badge for category '{category.name}'")
                created_count += 1

    print(f"Finished creating {created_count} badges.")

if __name__ == '__main__':
    create_initial_badges()
