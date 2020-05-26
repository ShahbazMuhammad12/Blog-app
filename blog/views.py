from django.shortcuts import render, redirect
from .forms import Registrationform
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import BlogApp
from .models import *
def home(request):
    return render(request, 'home.html')


def blogs(request):
    posts = Blog.objects.all()
    return render(request,'post.html',{'posts':posts})


def blogging(request):
    form = BlogApp(request.POST)
    if form.is_valid():
        form.save()
        return redirect('post')
    else:
            form = BlogApp()
    return render(request,'home.html',{'form':form})