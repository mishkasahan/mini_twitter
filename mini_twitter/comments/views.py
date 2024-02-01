from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm


def show_comments(request):
    all_comments = Comment.objects.all()
    context = {"all_comments": all_comments, "title": "Наші коменти"}
    return render(request, 'comments/comments_list.html', context)


def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            post = form.save()
            return redirect("/comments/all_comments")
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {"form": form})