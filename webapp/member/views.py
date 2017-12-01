from .models import UserProfile, User
from .serializers import UserEditSerializer, \
    UserProfileSerializer, \
    UserProfileEditSerializer, \
    UserDetailSerializer, \
    UserEnrollementsSerializer
from rest_framework.response import Response
from rest_framework import mixins, generics
from books.models import Book

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


class UserEnrollmentsAddView(mixins.RetrieveModelMixin,
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
