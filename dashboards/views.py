from django.shortcuts import redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    category_count=Category.objects.all().count()
    post_count=Blog.objects.all().count()
    context={
        "category_count":category_count,
        "post_count":post_count,
    }
    return render(request,'dashboards/dashboard.html',context)

def categories(request):
    return render(request,"dashboards/categories.html")

def add_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm()
    context={
        "form":form,
    }
    return render(request,"dashboards/add_category.html",context)

def edit_category(request,pk):
    category = Category.objects.get(pk=pk)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
        return redirect('categories')

    form = CategoryForm(instance=category)
    context={
        "form":form,
        "category":category,
    }
    return render(request,"dashboards/edit_category.html",context)

def delete_category(request,pk):
    category=Category.objects.get(pk=pk)
    category.delete()
    return redirect('categories')
