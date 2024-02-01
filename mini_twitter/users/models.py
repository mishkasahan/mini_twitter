from django.db import models


class User(models.Model):
    username = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=120, null=True, blank=True)
    city_of_residence = models.CharField(max_length=120, null=True, blank=True)
    marital_status = models.CharField(max_length=120, null=True, blank=True)
    phone_number = models.IntegerField( null=True, blank=True)
    email = models.EmailField(max_length=120)
    day_of_birth = models.DateField( null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_images = models.ImageField(upload_to="users/profile_images", null=True, blank=True)

    def __str__(self):
        return f"{self.username}"
