from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()
