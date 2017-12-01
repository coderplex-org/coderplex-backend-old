from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^user/profile', views.UserProfileView.as_view()),
    url(r'^user', views.UserDetailView.as_view()),
]
