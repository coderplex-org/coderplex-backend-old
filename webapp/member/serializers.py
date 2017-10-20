from member.models import User
from rest_framework import serializers


class UserSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')