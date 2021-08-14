from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=False)
    title = models.CharField(max_length=150)
    body = models.TextField()
    img = models.URLField()
    created_at = models.DateTimeField()
