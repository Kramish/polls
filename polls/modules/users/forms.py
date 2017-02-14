from django.contrib.auth.forms import User

from modules.base.forms import PollsFormMixin


class UserProfileForm(PollsFormMixin):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
