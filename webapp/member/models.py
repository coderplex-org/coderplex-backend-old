from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user")
    # I would prefer storing the image in S3 blob storage and saving the URL of the resource
    avatar = models.URLField(blank=False, null=False, max_length=100)
    mobile_number = models.CharField(max_length=20, blank=True, null=False, default="")
    short_bio = models.CharField(max_length=255, blank=False, null=False)
    job_status = models.BooleanField(blank=False, null=False, default=False)
    company_name = models.CharField(blank=True, null=False, default="", max_length=50)
    looking_for_job = models.BooleanField(blank=False, null=False, default=True)
    github_profile = models.URLField(blank=True, null=False, default="", max_length="50")
    facebook_profile = models.URLField(blank=True, null=False, default="", max_length="50")
    twitter_profile = models.URLField(blank=True, null=False, default="", max_length="50")
    linkedin_profile = models.URLField(blank=True, null=False, default="", max_length="50")
    codepen_profile = models.URLField(blank=True, null=False, default="", max_length="50")
    discord_username = models.CharField(blank=False, null=False, default="", max_length="25")
    # I think it would be costly to have a separate table for technologies, separate technologies with ;
    familiar_technologies = models.CharField(blank=True, null=False, default="", max_length=255)
    interested_technologies = models.CharField(blank=False, null=False, default="", max_length=255)


class Projects(models.Model):
    """
    Have a foreign key relationship with user for one-to-many relationship. Filter project based on user

    """
    pass


class Curriculum(models.Model):
    """
    User Foreign Key and all details regarding a particular curriculum [one-to-many again]
    """
    pass
