# quiz/views.py
import random
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required




def QuizPage(request):
    courses = Course.objects.all()
    return render(request, 'quizpage.html', {'courses': courses})

def quiz(request, course_id):
    course = Course.objects.get(pk=course_id)
    questions = list(Question.objects.filter(course=course))
    random.shuffle(questions)  # Shuffle the questions
    return render(request, 'quiz.html', {'course': course, 'questions': questions})

def submit_quiz(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(pk=course_id)
        questions = Question.objects.filter(course=course)
        total_questions = questions.count()
        correct_answers = 0

        for question in questions:
            submitted_option = request.POST.get(f"question_{question.id}")
            if submitted_option == question.correct_option:
                correct_answers += 1

        percentage_score = (correct_answers / total_questions) * 100

        # Save the score to the database
        score_instance = Score.objects.create(
            user=request.user,
            course=course,
            score=percentage_score
        )
        
        
        return redirect('quiz:show_score')  # Redirect to home page after submitting the quiz
    return redirect('quiz:home')
@login_required
def show_score(request):
    user_score = Score.objects.filter(user=request.user).order_by('-id').first()
    print(user_score)  # Add this line for debugging
    return render(request, 'score.html', {'user_score': user_score})

@login_required
def scores(request):
    user_scores = Score.objects.filter(user=request.user)
    return render(request, 'allscore.html', {'user_scores': user_scores})


