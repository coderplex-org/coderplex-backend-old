from rest_framework import viewsets
from .models import Book, Chapter, Page
from .serializers import BookSerializer, BookDetailSerializer, \
    ChapterSerializer, ChapterDetailSerializer, PageDetailSerializer
from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework.generics import get_object_or_404

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookDetailSerializer(instance)
        return Response(serializer.data)


class BookDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ChapterDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = ChapterDetailSerializer
    queryset = Chapter.objects.all()

    def get_object(self):
        return get_object_or_404(
            Chapter,
            book__slug=self.kwargs['book'],
            slug=self.kwargs['chapter'])

    def get(self, request, book, chapter, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PageDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = PageDetailSerializer
    queryset = Page.objects.all()

    def get_object(self):
        return get_object_or_404(
            Page,
            chapter__slug=self.kwargs['chapter'],
            slug=self.kwargs['slug'])

    def get(self, request, chapter, slug, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ChapterViewSet(viewsets.ModelViewSet):
    model = Chapter
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()
