from rest_framework import serializers
from member.serializers import UserShortSerializer
from .models import Book, Chapter, Page


class BookSerializer(serializers.ModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'slug', 'image', 'description', 'updated_at',
                  'updated_by', 'created_by')
        

class ChapterSerializer(serializers.ModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()
    
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'slug', 'content', 'updated_at',
                  'updated_by', 'created_by')


class PageSerializer(serializers.ModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()
    
    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'content', 'updated_at',
                  'updated_by', 'created_by')


class PageDetailSerializer(serializers.ModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()
    
    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'content', 'updated_at',
                  'updated_by', 'created_by')


class PageShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'updated_at')


class ChapterDetailSerializer(serializers.ModelSerializer):
    pages = serializers.SerializerMethodField()
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()
    
    def get_pages(self, obj):
        pages = Page.objects.filter(chapter=obj).order_by('position')
        return PageShortSerializer(pages, many=True).data

    class Meta:
        model = Chapter
        fields = ('id', 'title', 'slug', 'content', 'updated_at', 'pages',
                  'updated_by', 'created_by')


class ChapterShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'slug', 'updated_at')
        
        
class BookDetailSerializer(serializers.ModelSerializer):
    chapters = serializers.SerializerMethodField()
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()
    
    def get_chapters(self, obj):
        chapters = Chapter.objects.filter(book=obj).order_by('position')
        return ChapterShortSerializer(chapters, many=True).data

    class Meta:
        model = Book
        fields = ('id', 'title', 'slug', 'image', 'description', 'chapters',
                  'updated_by', 'created_by')
