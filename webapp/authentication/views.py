from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.linkedin_oauth2.views import LinkedInOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter

class LinkedinLogin(SocialLoginView):
    adapter_class = LinkedInOAuth2Adapter