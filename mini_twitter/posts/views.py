from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from comments.models import Comment


def show_posts(request, username=None):
    if username is not None:
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


def show_post(request, id=None):
    posts = [get_object_or_404(Post, id=id)]
    comments = Comment.objects.filter(post_id=id)
    context = {"posts": posts, "title": f"Пост № {id}", "comments": comments}
    return render(request, 'posts/show_post.html', context)



