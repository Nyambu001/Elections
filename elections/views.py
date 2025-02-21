from django.shortcuts import render
from .models import *


def index(request):
    recent_posts = Blog.objects.order_by('-date')[:3]
    videos = YouTubeVideo.objects.all()
    advertisements = Advertisement.objects.all()
    context = {
        'recent_posts': recent_posts,
        'videos': videos,
        'ads': advertisements
               }
    return render(request,'index.html', context)


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)

