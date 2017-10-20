from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Chapter
from .serializers import BookSerializer, BookDetailSerializer, ChapterSerializer, ChapterShortSerializer
from rest_framework.response import Response
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
