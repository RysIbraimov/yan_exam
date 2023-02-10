import requests
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Post, Comment, GradePost
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, CommentSerializer, PostRateSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:

            post = serializer.save(author=self.request.user.author)

            if post.author.telegram_chat_id:
                bot_token = "6056156320:AAFeKgSp8PhbG7723O4kKLxeCi9lNHQ7M6o"
                chat_id = post.author.telegram_chat_id
                message = f"Successful publication of post '{post.text}'"
                url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
                requests.post(url)
        else:
            return Response({'error':'вы не зарегистрированы!'})


class CommentCreateApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        post = Post.objects.filter(pk=self.kwargs.get('post_id')).first()
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user.author,post=post)
        else:
            temporary_username = self.request.data.get('comment_author','brha')
            serializer.save(temporary_username=temporary_username,post=post)


class CommentRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser, ]

    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs.get('post_id').first())


class RatePostApiView(viewsets.ModelViewSet):
    queryset = GradePost.objects.all()
    serializer_class = PostRateSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

    def get_queryset(self):
        return GradePost.objects.filter(post_id=self.kwargs['post_id'])


    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author, post_id=self.kwargs.get('post_id'))


