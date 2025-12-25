from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category,Blog,Comment
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
    if request.method == 'POST':
        comment=Comment()
        comment.user=request.user
        comment.blog=single_blog
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments=Comment.objects.filter(blog=single_blog)
    comment_count=Comment.objects.all().count()
    context={
        "single_blog":single_blog,
        "comments":comments,
        "comment_count":comment_count,
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