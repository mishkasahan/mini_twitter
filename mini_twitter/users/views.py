from django.shortcuts import render
from .models import User
from posts.models import Post


def show_users(request):
    all_users = User.objects.all()
    context = {"all_users": all_users, "title": "Наші юзери"}
    return render(request, 'users/users_list.html', context)


def show_user(request, username=None):
    user = User.objects.get(username=username)

    if username:
        posts = Post.objects.filter(user__username=username)
    else:
        posts = Post.objects.all()
    context = {"posts": posts, "user": user}
    return render(request, 'users/user_page.html', context)
