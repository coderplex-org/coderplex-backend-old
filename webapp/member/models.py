from django.db import models
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


# Create your models here.
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


# def create_user_profile(sender, instance, created, **kwargs):
#     """
#     This is a post save signal of django user inbuilt model triggers this method.
#     :param sender: The model which is responsible for the signal
#     :param instance: The instance that was just saved
#     :param created: The variable to check if the instance was created
#     :param kwargs: other Key value arguments
#     """
#     if created:
#         UserProfile.objects.create(user=instance)

@receiver(user_signed_up)
def retrieve_social_data(request, user, sociallogin=None, **kwargs):
    """Signal, that gets extra data from sociallogin and put it to profile."""
    # get the profile where i want to store the extra_data
    print (sociallogin.account.provider)  # e.g. 'twitter'
    print (sociallogin.account.get_avatar_url())
    print (sociallogin.account.get_profile_url())
    if sociallogin:
        avatar_url = sociallogin.acc22ount.get_avatar_url()

    profile = UserProfile(user=user, avatar = avatar_url)
    # in this signal I can retrieve the obj from SocialAccount
    profile.save()


# post_save.connect(create_user_profile, sender=User)
