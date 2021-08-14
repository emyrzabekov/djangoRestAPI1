from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.Serializer):

    owner = UserSerializer(read_only=True)
    title = serializers.CharField()
    body = serializers.CharField()
    img = serializers.URLField()
    created_at = serializers.DateTimeField(format='%d:%m:%Y %H:%M', input_formats=['%d:%m:%Y %H:%M'])

