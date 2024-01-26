from django.shortcuts import render
from .models import User


def show_users(request):
    all_users = User.objects.all()
    context = {"all_users": all_users, "title": "Наші юзери"}
    return render(request, 'users/users_list.html', context)
