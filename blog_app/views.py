from rest_framework import viewsets, permissions
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        blog = Blog.objects.get(pk=self.request.data['blog_pk'])
        comment = serializer.save()
        blog.comments.add(comment)
        blog.save()
