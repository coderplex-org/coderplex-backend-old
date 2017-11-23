from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.linkedin_oauth2.views import LinkedInOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from rest_framework import permissions

class GithubLogin(SocialLoginView):
    permission_classes = (permissions.IsAuthenticated,)
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.GITHUB_CALLBACK_URL

class LinkedinLogin(SocialLoginView):
    permission_classes = (permissions.IsAuthenticated,)
    adapter_class = LinkedInOAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.LINKEDIN_CALLBACK_URL