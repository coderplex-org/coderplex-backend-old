from .models import UserProfile, User
from .serializers import UserEditSerializer, UserProfileSerializer, UserProfileEditSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework import mixins, generics

# Create your views here.

class UserDetailView(mixins.RetrieveModelMixin,
                     generics.GenericAPIView):

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

class UserProfileView(mixins.RetrieveModelMixin,
                     generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(UserProfile.objects.get(user=request.user))
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserProfileEditSerializer(UserProfile.objects.get(user=request.user), data=request.data, user=request.user)

        if serializer.is_valid():
            serializer.save()
            profile_serializer = UserProfileSerializer(UserProfile.objects.get(user=request.user))
            return Response(profile_serializer.data)

        else:
            return Response(serializer.errors)