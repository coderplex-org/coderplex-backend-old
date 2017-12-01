from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/profile', views.UserProfileView.as_view()),
    url(r'^user/enrollments/delete',
        views.UserEnrollmentsDeleteView.as_view()),
    url(r'^user/enrollments/add', views.UserEnrollmentsAddView.as_view()),
    url(r'^user/enrollments', views.UserEnrollmentsView.as_view()),
    url(r'^user', views.UserDetailView.as_view()),
]
