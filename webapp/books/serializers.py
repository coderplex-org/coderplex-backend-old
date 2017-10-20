from rest_framework import serializers
from .models import CurriculumBook


class CurriculumBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumBook
        fields = ('id', 'title', 'slug', 'image', 'description', 'updated_at')