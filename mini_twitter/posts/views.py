from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Comment


def show_posts(request):
    all_posts = Post.objects.all()
    context = {"all_posts": all_posts, "title": "Наші пости"}
    return render(request, 'posts/posts_list.html', context)


def show_coments(request):
    all_coments = Comment.objects.all()
    context = {"all_coments": all_coments, "title": "Наші коменти"}
    return render(request, 'coments/coments_list.html', context)
