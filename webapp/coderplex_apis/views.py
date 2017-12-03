from rest_framework import views
from rest_framework import response
from rest_framework import permissions


class HelloWorldView(views.APIView):
    # TODO: Move this to some generic app
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, request, **kwargs):
        return response.Response({"message": "Hello World!"})


class SocialCodeView(views.APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, request, **kwargs):
        return response.Response({"code": request.GET.get('code')})
