from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Category,Blog

# Create your views here.
def posts_by_category(request,category_id):
    posts=Blog.objects.filter(status="Published",category_id=category_id)
    try:
        category=Category.objects.get(pk=category_id)
    except:
        return redirect("home")
    context={
        "posts":posts,
        "category":category,
    }
    return render(request,"posts_by_category.html",context)