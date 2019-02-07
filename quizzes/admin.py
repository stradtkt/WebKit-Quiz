from django.contrib import admin
from .models import *


class QuizCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_category']
    raw_id_fields = ('category',)

    def get_category(self, obj):
        return obj.category.category

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'get_quiz']
    raw_id_fields = ('quiz',)

    def get_quiz(self, obj):
        return obj.quiz.name

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('choice', 'is_right', 'get_question')
    raw_id_fields = ('question',)

    def get_question(self, obj):
        return obj.question.question



admin.site.register(QuizCategory, QuizCategoryAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)