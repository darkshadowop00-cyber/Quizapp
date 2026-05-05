from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('quiz/<slug:quiz_slug>/', views.quiz_take, name='quiz_take'),
    path('quiz/<slug:quiz_slug>/result/', views.quiz_result, name='quiz_result'),
]
