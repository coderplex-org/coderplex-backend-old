from rest_framework import serializers
from .models import Book, Chapter
from member.serializers import UserSerializerShort


class BookSerializer(serializers.ModelSerializer):
    created_by = UserSerializerShort()
    updated_by = UserSerializerShort()
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'slug', 'image', 'description', 'updated_at',
                  'updated_by', 'created_by')
        

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'slug', 'updated_at')
        
        
class BookDetailSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True)
    created_by = UserSerializerShort()
    updated_by = UserSerializerShort()
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'slug', 'image', 'description', 'chapters',
                  'updated_by', 'created_by')
