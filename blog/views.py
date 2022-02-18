from django.shortcuts import render
from home.models import Content
from blog.models import Blog

# Create your views here.

def blog(request):
    blog=Blog.objects.all()
    blog={'blogs':blog}
    return render(request,'blog/blog.html',blog)


def blogPost(request,slug):
    return render(request,'blog/blogpost.html')