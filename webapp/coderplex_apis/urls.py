"""coderplex_apis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import views
from rest_framework import response


class HelloWordView(views.APIView):
    # TODO: Move this to some generic app

    def get(self, request, **kwargs):
        return response.Response({"message": "Hello World!"})


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('books.urls')),
    url(r'^$', HelloWordView.as_view()),
]
