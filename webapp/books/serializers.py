from rest_framework import serializers
from member.serializers import UserSerializerShort
from .models import Book, Chapter, Page


class BookSerializer(serializers.ModelSerializer):
    created_by = UserSerializerShort()
    updated_by = UserSerializerShort()
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'slug', 'image', 'description', 'updated_at',
                  'updated_by', 'created_by')
        

class ChapterSerializer(serializers.ModelSerializer):
    created_by = UserSerializerShort()
    updated_by = UserSerializerShort()
    
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'slug', 'content', 'updated_at',
                  'updated_by', 'created_by')


class PageSerializer(serializers.ModelSerializer):
    created_by = UserSerializerShort()
    updated_by = UserSerializerShort()
    
    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'content', 'updated_at',
                  'updated_by', 'created_by')


class ChapterDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializerShort()
    updated_by = UserSerializerShort()
    pages = PageSerializer(many=True)
    
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'slug', 'content', 'updated_at', 'pages',
                  'updated_by', 'created_by')


class ChapterShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'slug', 'updated_at')
        
        
class BookDetailSerializer(serializers.ModelSerializer):
    chapters = ChapterShortSerializer(many=True)
    created_by = UserSerializerShort()
    updated_by = UserSerializerShort()
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'slug', 'image', 'description', 'chapters',
                  'updated_by', 'created_by')
