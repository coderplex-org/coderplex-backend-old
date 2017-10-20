from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^books$', views.BookViewSet.as_view({'get': 'list'})),
    url(r'^book/(?P<pk>[0-9]+)$', views.BookViewSet.as_view({'get': 'retrieve'})),

    url(r'^chapters$', views.ChapterViewSet.as_view({'get': 'list'})),
    url(r'^chapter/(?P<pk>[0-9]+)$', views.ChapterViewSet.as_view({'get': 'retrieve'})),
]