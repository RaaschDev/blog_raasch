from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()

    context = {
        "posts":posts
    }
    return render(request, 'blog/home.html', context=context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post":post
    }

    return render(request, 'blog/detail.html', context=context)