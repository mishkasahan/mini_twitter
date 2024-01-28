from django.shortcuts import render
from .models import Post,Comment


def show_posts(request, username=None):
    if username:
        posts = Post.objects.filter(user__username=username)
    else:
        posts = Post.objects.all()
    context = {"posts": posts, "title": "Наші пости"}
    return render(request, 'posts/posts_list.html', context)


def show_coments(request):
    all_coments = Comment.objects.all()
    context = {"all_coments": all_coments, "title": "Наші коменти"}
    return render(request, 'coments/coments_list.html', context)
