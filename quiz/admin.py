from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Unregister the default User admin
admin.site.unregister(User)

# Define a new User admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)

from .models import Category, Quiz, Question, Answer, Badge, UserProfile

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Badge)
admin.site.register(UserProfile)
