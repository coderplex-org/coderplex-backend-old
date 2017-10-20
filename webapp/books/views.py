from django.shortcuts import render
from rest_framework import viewsets
from .models import CurriculumBook
from .serializers import CurriculumBookSerializer
# Create your views here.


class CurriculumBookViewset(viewsets.ModelViewSet):
    model = CurriculumBook
    serializer_class = CurriculumBookSerializer
    queryset = CurriculumBook.objects.all()
