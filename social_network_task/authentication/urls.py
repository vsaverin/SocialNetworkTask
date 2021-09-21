from django.urls import path

from .views import (
    RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, PostList, PostDetail
    )

app_name = 'authentication'
urlpatterns = [
    path('user', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
]