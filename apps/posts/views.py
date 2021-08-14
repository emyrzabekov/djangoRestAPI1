from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        tasks = Post.objects.all()
        serializer = PostSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            owner = request.user
            task = Post.objects.create(
                owner=owner,
                title=serializer.validated_data.get('title'),
                body=serializer.validated_data.get('body'),
                img=serializer.validated_data.get('img'),
                created_at=serializer.validated_data.get('created_at'),
            )
            serializer = PostSerializer(instance=task)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
