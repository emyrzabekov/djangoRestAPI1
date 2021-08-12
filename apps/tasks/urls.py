from django.urls import path
from apps.tasks.views import TaskAPIView


urlpatterns = [
    path('', TaskAPIView.as_view()),

]
