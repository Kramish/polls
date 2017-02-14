from django.contrib import admin

from .models import Choice, Answer, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    ordering = ('id',)


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    can_delete = False

    def has_add_permission(self, request):
        return False
    

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    inlines = (ChoiceInline,)
    readonly_fields = ('pub_date',)
