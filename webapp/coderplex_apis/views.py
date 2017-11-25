from rest_framework import views
from rest_framework import response

class HelloWordView(views.APIView):
    # TODO: Move this to some generic app

    def get(self, request, **kwargs):
        return response.Response({"message": "Hello World!"})

class SocialCodeView(views.APIView):

    def get(self, request, **kwargs):
        return response.Response({"code": request.GET.get('code')})