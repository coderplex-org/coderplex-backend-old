from django.db import models
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth import login

class UserProfile(models.Model):
    """
    This model is an extension of the User model that is inbuilt in django.
    It is connected to django User model with a OneToOneField.
    """
    user = models.OneToOneField(User, related_name="user")
    avatar = models.URLField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True, default=None)
    short_bio = models.CharField(max_length=255, blank=True, null=True, default=None)
    job_status = models.NullBooleanField(blank=True, null=True, default=None)
    company_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    looking_for_job = models.NullBooleanField(blank=True, null=True, default=None)
    github_profile = models.URLField(max_length=75, blank=True, null=True, default=None)
    facebook_profile = models.URLField(max_length=75, blank=True, null=True, default=None)
    twitter_profile = models.URLField(max_length=75, blank=True, null=True, default=None)
    linkedin_profile = models.URLField(max_length=75, blank=True, null=True, default=None)
    codepen_profile = models.URLField(max_length=75, blank=True, null=True, default=None)
    discord_profile = models.CharField(max_length=25, blank=True, null=True, default=None)
    familiar_technologies = models.CharField(max_length=255, blank=True, null=True, default=None)
    interested_technologies = models.CharField(max_length=255, blank=True, null=True, default=None)

@receiver(user_signed_up)
def retrieve_social_data(request, user, sociallogin=None, **kwargs):
    """Signal, that gets extra data from sociallogin and put it to profile."""

    if sociallogin:
        print("provider",sociallogin.account.provider)
        print("extra_data", sociallogin.account.extra_data)

        avatar_url = sociallogin.account.get_avatar_url()
        profile, created = UserProfile.objects.get_or_create(user=user)

        if sociallogin.account.provider == 'github':
            present_user = User.objects.filter(email=user.email)[0]
            profile = UserProfile.objects.filter(user=present_user)[0]
            profile.github_profile = sociallogin.account.get_profile_url()
            profile.short_bio = sociallogin.account.extra_data["bio"]
            profile.job_status = sociallogin.account.extra_data["hireable"]
            profile.company_name = sociallogin.account.extra_data["company"]
            profile.save()
        elif sociallogin.account.provider == 'linkedin_oauth2':
            present_user = User.objects.filter(email=user.email)[0]
            profile = UserProfile.objects.filter(user=present_user)[0]
            profile.linkedin_profile = sociallogin.account.get_profile_url()
            profile.short_bio = sociallogin.account.extra_data["headline"],
            profile.save()

        # login(request, user)
    # in this signal I can retrieve the obj from SocialAccount