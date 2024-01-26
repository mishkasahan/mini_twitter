from django.urls import path
from .views import show_users

urlpatterns = [
    path('', show_users, name="show_users"),
    path('', show_users, name="show_users")
    ]