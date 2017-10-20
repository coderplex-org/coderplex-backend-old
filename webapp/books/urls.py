from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^books$', views.CurriculumBookViewset.as_view({'get': 'list'})),
    url(r'^books/(?P<pk>[0-9]+)$', views.CurriculumBookViewset.as_view({'get': 'retrieve'})),
]