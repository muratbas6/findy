from django.shortcuts import render, HttpResponse
from get_info import *
from users.models import User


# Create your views here.

def mainPage_view(request):
    user = User.objects.all()
    return render(request, "main.html", {"user": user})
