from django.conf.urls import url

from .views import UserProfileView, SessionView


urlpatterns = [
    url(r'^$', UserProfileView.as_view(), name='index'),
    url(r'^session/$', SessionView.as_view(), name='session')
]
