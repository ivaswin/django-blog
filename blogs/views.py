from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Blog,Category

# Create your views here.

def posts_by_category(request,category_id):
    posts = Blog.objects.filter(status = "Published",category= category_id)

    # use try and excepty block if you want to do some custom actions if category dosesnot exist
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    
    # Use get_object_or_404 if you want to show the 404 error page if category doesnot exist
    category = get_object_or_404(Category,pk = category_id)

    context ={
        "posts" : posts,
        "category" :category,
    }
    return render(request,'posts_by_category.html',context)
