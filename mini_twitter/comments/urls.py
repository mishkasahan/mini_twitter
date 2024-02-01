from django.urls import path
from .views import show_comments, add_comment

urlpatterns = [
    path('all_comments/', show_comments, name="show_comments"),
    path('add-comment/', add_comment, name="add_comment"),
]