from django.db import models

# Create your models here.

class QuizCategory(models.Model):
    category = models.CharField(unique=True, max_length=255)


class Quiz(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(QuizCategory)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    question = models.CharField(max_length=255)

    
class Answer(models.Model):
    question = models.ForeignKey(Question)
    is_right = models.BooleanField()
    choice = models.CharField(max_length=255)