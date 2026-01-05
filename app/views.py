from django.shortcuts import render
from .models import Category, Video
# Create your views here.

def home_page(request):
    categories = Category.objects.all()
    videos = Video.objects.all()
    context = {
        'categories': categories,
        'videos': videos
    }
    return render(request, 'home.html', context)

def category_page(request, pk):
    categories = Category.objects.get(id=pk)
    videos = Video.objects.filter(video_category=categories)
    context = {
        'categories': categories,
        'videos': videos
    }
    return render(request, 'category.html', context)

def video_page(request, pk):
    videos = Video.objects.get(id=pk)
    context = {
        'videos': videos
    }
    return render(request, 'video.html', context)
