from django.urls import path
from .views import show_posts, show_coments, add_post

urlpatterns = [
    path('', show_posts, name="show_posts"),
    path('<str:username>/', show_posts, name='show_posts'),
    path('coments/', show_coments, name="show_coments"),
    path('add_post/', add_post, name="add_post")
]