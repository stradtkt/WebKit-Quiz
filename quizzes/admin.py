from django.contrib import admin
from . import models


class QuestionInline(admin.StackedInline):
    model = models.Question

class QuizInline(admin.StackedInline):
    model = models.Quiz

class AnswerInline(admin.TabularInline):
    model = models.Answer

class QuizCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline,]
    list_display = ['name', 'get_category']
    raw_id_fields = ('category',)

    def get_category(self, obj):
        return obj.category.category

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]
    list_display = ['question', 'get_quiz']
    raw_id_fields = ('quiz',)

    def get_quiz(self, obj):
        return obj.quiz.name


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('choice', 'is_right', 'get_question')
    raw_id_fields = ('question',)

    def get_question(self, obj):
        return obj.question.question

admin.site.register(models.QuizCategory, QuizCategoryAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Answer, AnswerAdmin)