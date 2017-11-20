from rest_framework import serializers


class GitHubCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100)