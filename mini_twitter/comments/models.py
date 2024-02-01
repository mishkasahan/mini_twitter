from django.db import models


class Comment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    content = models.TextField()
    comment_photo = models.ImageField(upload_to="comments/comments_photo", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
