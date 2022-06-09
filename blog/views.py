from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html',{'blogs':blogs})

def detail(request,blog_id):   
     detailblog = get_object_or_404(Blog, pk=blog_id)
     return render(request,'blog/detail.html',{'blog':detailblog})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image']:
            blog = Blog()
            blog.title = request.POST['title']
            blog.body = request.POST['body']
            blog.image = request.FILES['image']
            blog.pub_date = timezone.datetime.now()
            blog.save()
            return redirect('/blog/')
        else:
            return render(request, 'blog/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'blog/create.html')