from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, null=False)
    pub_date = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    choice_text = models.CharField(max_length=200, null=False)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    answer_date = models.DateTimeField(null=False, default=timezone.now)
