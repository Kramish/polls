from django import forms
from django.contrib.auth.forms import User

from modules.base.forms import PollsFormMixin


class UserProfileForm(PollsFormMixin):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
