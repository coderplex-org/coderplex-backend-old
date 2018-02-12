from .models import UserProfile, User
from .serializers import UserEditSerializer, \
    UserProfileSerializer, \
    UserProfileEditSerializer, \
    UserDetailSerializer, \
    UserEnrollementsSerializer, \
    UserBooksSerializer

from rest_framework.response import Response
from rest_framework import mixins, generics
from books.models import Book
from books.serializers import BookSerializer
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


class UserDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):

    model = User
    serializer_class = UserDetailSerializer

    def get(self, request, *args, **kwargs):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserEditSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserProfileView(mixins.RetrieveModelMixin, generics.GenericAPIView):

    model = UserProfile
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user)
        serializer = UserProfileEditSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)


class UserEnrollmentsView(mixins.RetrieveModelMixin, generics.GenericAPIView):

    model = UserProfile
    serializer_class = UserEnrollementsSerializer

    def get(self, request, *args, **kwargs):
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user)
        serializer = UserEnrollementsSerializer(user_profile)
        return Response(serializer.data)


class UserEnrollmentsCreateView(mixins.RetrieveModelMixin,
                                generics.GenericAPIView):

    model = UserProfile
    serializer_class = UserEnrollementsSerializer

    def post(self, request, *args, **kwargs):
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user)
        book = Book.objects.filter(slug=request.data["slug"])[0]
        user_profile.enrollments.add(book)
        serializer = UserEnrollementsSerializer(user_profile)
        return Response(serializer.data)


class UserEnrollmentsDeleteView(mixins.RetrieveModelMixin,
                                generics.GenericAPIView):

    model = UserProfile
    serializer_class = UserEnrollementsSerializer

    def post(self, request, *args, **kwargs):
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user)
        book = Book.objects.filter(slug=request.data["slug"])[0]
        user_profile.enrollments.remove(book)
        serializer = UserEnrollementsSerializer(user_profile)
        return Response(serializer.data)


class UserBooksView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    model = User
    serializer_class = UserBooksSerializer

    def get(self, request, *args, **kwargs):
        serializer = UserBooksSerializer(
            request.user, context={
                'request': request
            })
        return Response(serializer.data)


class UserBooksCreateView(mixins.RetrieveModelMixin, generics.GenericAPIView):

    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        request.user.books.create(
            title=request.data["title"],
            description=request.data["description"],
            slug=request.data["title"].lower(),
            updated_by=request.user)
        serializer = UserBooksSerializer(
            request.user, context={
                'request': request
            })
        return Response(serializer.data)


class UserBooksDeleteView(mixins.RetrieveModelMixin, generics.GenericAPIView):

    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        try:
            book = Book.objects.filter(slug=request.data["slug"])[0]
            if book.created_by == request.user:
                book.delete()
                return Response({
                    "message":
                    "The Book " + request.data["slug"] + " is deleted"
                })
            else:
                return Response({
                    "message":
                    "The Book " + request.data["slug"] + " is not owned by you"
                })

        except ObjectDoesNotExist:
            return Response({
                "message":
                "The Book " + request.data["slug"] + " doesn't exist"
            })
