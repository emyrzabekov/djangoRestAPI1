from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username',]


# class TaskSerializer(serializers.Serializer):

    # owner = UserSerializer(read_only=True)
    # body = serializers.CharField()
    # deadline = serializers.DateTimeField(format='%d:%m:%Y %H:%M', input_formats=['%d:%m:%Y %H:%M', ])
    # is_finished = serializers.BooleanField(read_only=True)

# Так было раньше... теперь будет все подругому

class TaskSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(format='%d:%m:%Y %H:%M', input_formats=['%d:%m:%Y %H:%M', ])
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'owner', 'body', 'deadline', 'is_finished']
        read_only_fields = ['is_finished',]