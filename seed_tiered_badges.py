import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz.models import Category, Badge

def create_tiered_badges():
    # Delete existing badges to start fresh
    Badge.objects.all().delete()
    print("Deleted all existing badges.")

    categories = Category.objects.all()
    created_count = 0

    tier_configs = [
        ('BRONZE', 60, '🥉', 'Initiate'),
        ('SILVER', 80, '🥈', 'Specialist'),
        ('GOLD', 100, '🥇', 'Master'),
    ]

    for category in categories:
        for tier, min_score, icon, suffix in tier_configs:
            name = f"{category.name} {suffix}"
            description = f"Achieved a score of {min_score}% or higher in {category.name}."
            
            # Custom names for some categories to make it feel premium
            if category.name == 'Python Basics' and tier == 'GOLD':
                name = 'Python Pioneer'
                description = 'Mastered the fundamentals of Python programming.'
                icon = '🐍'
            elif category.name == 'Django Views' and tier == 'GOLD':
                name = 'View Virtuoso'
                description = 'Perfectly understood Django class and function-based views.'
                icon = '🎯'

            Badge.objects.create(
                category=category,
                name=name,
                description=description,
                icon=icon,
                min_score=min_score,
                tier=tier
            )
            created_count += 1
            print(f"Created {tier} badge for {category.name}")

    print(f"Finished creating {created_count} badges.")

if __name__ == '__main__':
    create_tiered_badges()
