from django.db import models


class User(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_images = models.ImageField(upload_to="users/profile_images", null=True, blank=True)
