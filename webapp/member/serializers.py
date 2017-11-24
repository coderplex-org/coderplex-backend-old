from .models import User, UserProfile
from rest_framework import serializers

class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'avatar', 'mobile_number', 'short_bio', 'job_status', 'company_name', 'looking_for_job', 'github_profile', 'facebook_profile', 'twitter_profile', 'linkedin_profile', 'codepen_profile', 'discord_profile', 'familiar_technologies', 'interested_technologies')

class UserEditSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)

    def update(self, instance, validated_data):

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.email = validated_data.get('email', instance.email)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance

class UserProfileEditSerializer(serializers.Serializer):
    avatar = serializers.URLField(required=False)
    mobile_number = serializers.CharField(required=False)
    short_bio = serializers.CharField(required=False)
    job_status = serializers.NullBooleanField(required=False)
    company_name = serializers.CharField(required=False)
    looking_for_job = serializers.NullBooleanField(required=False)
    github_profile = serializers.URLField(required=False)
    facebook_profile = serializers.URLField(required=False)
    twitter_profile = serializers.URLField(required=False)
    linkedin_profile = serializers.URLField(required=False)
    codepen_profile = serializers.URLField(required=False)
    discord_profile = serializers.CharField(required=False)
    familiar_technologies = serializers.CharField(required=False)
    interested_technologies = serializers.CharField(required=False)

    def update(self, instance, validated_data, user):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)
        instance.short_bio = validated_data.get('short_bio', instance.short_bio)
        instance.job_status = validated_data.get('job_status', instance.job_status)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.looking_for_job = validated_data.get('looking_for_job', instance.looking_for_job)
        instance.github_profile = validated_data.get('github_profile', instance.github_profile)
        instance.facebook_profile = validated_data.get('facebook_profile', instance.facebook_profile)
        instance.twitter_profile = validated_data.get('twitter_profile', instance.twitter_profile)
        instance.linkedin_profile = validated_data.get('linkedin_profile', instance.linkedin_profile)
        instance.codepen_profile = validated_data.get('codepen_profile', instance.codepen_profile)
        instance.discord_profile = validated_data.get('discord_profile', instance.discord_profile)
        instance.familiar_technologies = validated_data.get('familiar_technologies', instance.familiar_technologies)
        instance.interested_technologies = validated_data.get('interested_technologies', instance.interested_technologies)
        instance.user = user
        instance.save()
        return instance