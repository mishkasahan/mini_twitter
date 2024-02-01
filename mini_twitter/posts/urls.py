from django.urls import path
from .views import show_posts, add_post, show_post

urlpatterns = [
    path('all-posts/', show_posts, name="show_posts"),
    path('add-post/', add_post, name="add_post"),
    path('show-post/<int:id>/', show_post, name="show_post"),
    path('<str:username>/', show_posts, name='show_posts'),
]