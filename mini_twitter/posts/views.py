from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm


def show_posts(request, username=None):
    if username:
        posts = Post.objects.filter(user__username=username)
    else:
        posts = Post.objects.all()
    context = {"posts": posts, "title": "Наші пости"}
    return render(request, 'posts/posts_list.html', context)


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            post = form.save()
            return redirect("posts/posts_list.htm")
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {"form": form})


def show_coments(request):
    all_coments = Comment.objects.all()
    context = {"all_coments": all_coments, "title": "Наші коменти"}
    return render(request, 'coments/coments_list.html', context)
