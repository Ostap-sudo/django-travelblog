from django.shortcuts import render, get_object_or_404
from .models import Post
from . import views


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html',  {'posts': posts})


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html') 

from django.shortcuts import render

def contact(request):
    return render(request, 'blog/contact.html')