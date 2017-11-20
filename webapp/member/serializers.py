from .models import User, UserProfile
from rest_framework import serializers


class UserDetailSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    def get_avatar(self, obj):
        return obj.profile.avatar

    class Meta:
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name', 'avatar')


class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserShortSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'avatar']