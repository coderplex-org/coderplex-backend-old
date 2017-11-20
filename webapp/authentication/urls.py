from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),

    url(r'^auth/github$', views.GithubLogin.as_view(), name='gh_login'),
    url(r'^accounts/', include('allauth.urls')),

]
