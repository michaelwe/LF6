from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response

from management.models import *


def show_users(request):
    users = Mitarbeiter.objects.all()
    return render_to_response("management/show_users.html", {"users": users})
