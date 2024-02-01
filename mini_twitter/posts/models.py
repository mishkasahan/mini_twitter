from django.db import models


class Post(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    post_photo = models.ImageField(upload_to="posts/posts_photo", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)




