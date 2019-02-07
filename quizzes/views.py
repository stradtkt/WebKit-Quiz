from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    quiz = Quiz.objects.all()
    context = {
        "quiz": quiz
    }
    return render(request, 'quizzes/index.html', context)

def view_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    context = {
        "quiz": quiz
    }
    return render(request, 'quizzes/view-quiz.html', context)

