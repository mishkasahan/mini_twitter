from django.urls import path
from .views import show_users, show_user

urlpatterns = [
    path('', show_users, name="show_users"),
    path('<str:username>/', show_user, name="show_user")
    ]