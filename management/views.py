from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response


def show_users(request):
    users = User.objects.all()
    return render_to_response("management/show_users.html", {"users": users})
