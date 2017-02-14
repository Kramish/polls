from django.views.generic import View


class SessionView(View):
    def get(self, request, *args, **kwargs):

        return c

    def post(self, request):
        pass


class UserProfileView(View):
    param1 = 5
    user = None

    def get(self, request, *args, **kwargs):
        print(UserProfileView().param1)
        pass

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        self.user = User(id=1)
        self.clear()
        self.validate()
        self.save()

    def validate(self):
        pass

    def clear(self):
        pass

    def save(self):
        pass
