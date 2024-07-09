from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_path = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE, null=True)
    text = models.TextField()
    date1 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.blog.user.username} on {self.blog.title}'
