from django.urls import path
from apps.posts.views import PostAPIView


urlpatterns = [
    path('posts/', PostAPIView.as_view()),
]