from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Chapter, Page
from .serializers import BookSerializer, BookDetailSerializer, ChapterSerializer, ChapterDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.db.models.query import QuerySet

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookDetailSerializer(instance)
        return Response(serializer.data)
    
    
class ChapterViewSet(viewsets.ModelViewSet):
    model = Chapter
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ChapterPagesListAPIView(APIView):
    
    def get(self, request, book, chapter, format=None, **kwargs):
        book = get_object_or_404(Book, pk=book) # TODO - slug or pk?
        chapter = get_object_or_404(Chapter, pk=chapter,)
        pages = chapter.pages.all()
        serializer = ChapterDetailSerializer(pages, many=True)
        return Response(serializer.data)