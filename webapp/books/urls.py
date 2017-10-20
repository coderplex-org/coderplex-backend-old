from django.conf.urls import url, include
from . import views

urlpatterns = [
    
    url(r'^books$', views.BookViewSet.as_view({'get': 'list'})),
    
    url(r'^book/(?P<slug>[-\w]+)$', views.BookDetailView.as_view()),
    url(r'^book/(?P<book>[-\w]+)/c/(?P<chapter>[-\w]+)$', views.ChapterDetailView.as_view()),
    
    
    # from viewset for the CRUD operations
    url(r'^chapters$', views.ChapterViewSet.as_view({'get': 'list'})),
    url(r'^chapter/(?P<pk>[-\w]+)$', views.ChapterViewSet.as_view({'get': 'retrieve'})),


]