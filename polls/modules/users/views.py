from collections import defaultdict
import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import View


class SessionView(View):
    # def get(self, request, *args, **kwargs):
    #     return c

    def post(self, request):
        error_message = defaultdict(str)

        username = request.POST.get('username')
        if not username:
            error_message['username'] = 'Username is required.'

        password = request.POST.get('password')
        if not password:
            error_message['password'] = 'Password is required.'

        data = {'status': 'ok'}

        if error_message:
            data = {
                'status': 'error',
                'errors': error_message
            }

        return JsonResponse(data)


class UserProfileView(View):
    param1 = 5
    user = None

    def get(self, request, *args, **kwargs):
        print(UserProfileView().param1)
        pass

    def post(self, request, *args, **kwargs):
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        user = User.objects.create_user(username=username, password=password,
                                        email=email)

    def put(self, request, *args, **kwargs):
        # self.user = User(id=1)
        # self.clear()
        # self.validate()
        # self.save()

        pass

    def validate(self):
        pass

    def clear(self):
        pass

    def save(self):
        pass
