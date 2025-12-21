from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogs.models import Category,Blog
from assignments.models import About
from .form import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    featured_posts=Blog.objects.filter(is_featured=True,status="Published").order_by("updated_at")
    posts=Blog.objects.filter(is_featured=False,status="Published")
    try:
        about=About.objects.get()
    except:
        about=None
    context={
        "featured_posts":featured_posts,
        "posts":posts,
        "about":about,
    }
    return render(request,"home.html",context)

def register(request):
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form=RegisterForm()
    context={
        "form":form,
    }
    return render(request,"register.html",context)


def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)

            return redirect('home')
    auth_form=AuthenticationForm()
    context={
        "auth_form":auth_form,
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')
