from .models import UserProfile, User
from .serializers import UserDetailSerializer, UserEditSerializer
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
