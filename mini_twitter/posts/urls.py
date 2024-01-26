from django.urls import path
from .views import show_posts,show_coments

urlpatterns = [
    path('', show_posts, name="show_posts"),
    path('coments/', show_coments, name="show_coments")
]