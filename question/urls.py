from django.urls import path
from .views import*
from question import views

app_name = 'quiz'
urlpatterns = [
    path('home/quizpage/', views.QuizPage, name='quizpage'),
    path('quiz/<int:course_id>/', views.quiz, name='quiz'),
    path('quiz/<int:course_id>/submit/', views.submit_quiz, name='submit_quiz'),
    path('score/', views.show_score, name='show_score'),
    path('scores/',views.scores, name='scores'),
    
]

