from django.db import models

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=50)
    

class Question(models.Model):
    quiz = models.ForeignKey(Quiz)

    
class Answer(models.Model):
    question = models.ForeignKey(Question)