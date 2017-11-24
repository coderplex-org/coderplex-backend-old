from .models import User, UserProfile
from rest_framework import serializers


class UserDetailSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    def get_avatar(self, obj):
        try:
            return obj.profile.avatar
        except:
            return ""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'avatar', 'email')


class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserShortSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'avatar']


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