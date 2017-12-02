from rest_framework import serializers
# from member.serializers import UserShortSerializer
from .models import Book, Chapter, Page

from member.models import User


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


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
        fields = ('id', 'title', 'slug', 'content', 'updated_at', 'updated_by',
                  'created_by')


class PageSerializer(serializers.ModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()

    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'content', 'updated_at', 'updated_by',
                  'created_by')


class PageDetailSerializer(serializers.ModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()

    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'content', 'updated_at', 'updated_by',
                  'created_by')


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


# The following serializers will be used for User Serializers


class UserPageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'content', 'updated_at')


class UserChapterDetailSerializer(serializers.ModelSerializer):
    pages = serializers.SerializerMethodField()

    def get_pages(self, obj):
        pages = Page.objects.filter(chapter=obj).order_by('position')
        return UserPageDetailSerializer(pages, many=True).data

    class Meta:
        model = Chapter
        fields = ('id', 'title', 'slug', 'content', 'updated_at', 'pages')


class UserBookDetailSerializer(serializers.ModelSerializer):
    chapters = serializers.SerializerMethodField()

    def get_chapters(self, obj):
        chapters = Chapter.objects.filter(book=obj).order_by('position')
        return UserChapterDetailSerializer(chapters, many=True).data

    class Meta:
        model = Book
        fields = ('id', 'title', 'slug', 'image', 'description', 'chapters')
