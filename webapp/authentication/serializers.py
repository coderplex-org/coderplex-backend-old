from rest_framework import serializers


class GitHubCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100)


class LinkedInCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100)
