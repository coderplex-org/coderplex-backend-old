from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer, BookDetailSerializer
from rest_framework.response import Response
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookDetailSerializer(instance)
        return Response(serializer.data)