from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=False)
    body = models.TextField()
    is_finished = models.BooleanField(default=False)
    deadline = models.DateTimeField()
