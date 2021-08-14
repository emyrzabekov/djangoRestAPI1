from django.urls import path, include
from apps.tasks.views import TaskCreateListView, TaskDetailGenericView, SetFinishedTaskAPIView


urlpatterns = [
    path('tasks_list/', TaskCreateListView.as_view()),
    # path('tasks_create/', TaskCreateView.as_view()),
    path('tasks/<int:id>/', TaskDetailGenericView.as_view()),
    # path('tasks/update/<int:id>/', TaskUpdateGenericView.as_view()),
    # path('tasks/delete/<int:id>/', TaskDestroyGenericView.as_view()),
    path('tasks/<int:id>/finished', SetFinishedTaskAPIView.as_view()),

]
