from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category,Blog
from django.db.models import Q

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

def single_blog_page(request,blog_slug):
    single_blog = get_object_or_404(Blog,slug=blog_slug,status="Published")
    context={
        "single_blog":single_blog
    }
    return render(request,"blogs.html",context)

def search(request):
    keyword=request.GET.get('keyword')
    search_result=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , status="Published" )
    context={
        "search_result":search_result,
        "keyword":keyword,
    }
    return render(request,'search.html',context)