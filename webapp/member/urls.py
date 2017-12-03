from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user$', views.UserDetailView.as_view()),
    url(r'^user/profile$', views.UserProfileView.as_view()),
    url(r'^user/enrollments$', views.UserEnrollmentsView.as_view()),
    url(r'^user/enrollments/add$', views.UserEnrollmentsCreateView.as_view()),
    url(r'^user/enrollments/delete$',
        views.UserEnrollmentsDeleteView.as_view()),
    url(r'^user/books$', views.UserBooksView.as_view()),
    url(r'^user/books/add$', views.UserBooksCreateView.as_view()),
    url(r'^user/books/delete$', views.UserBooksDeleteView.as_view())
]
