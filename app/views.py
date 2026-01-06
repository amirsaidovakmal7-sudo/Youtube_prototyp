from django.shortcuts import render, redirect
from .models import Category, Video, AddVideo
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View
from . import forms
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


def search(request):
    if request.method == 'POST':
        search_video = request.POST['search-video']
        get_video = Video.objects.filter(news_video_name__iregex=search_video)
        context = {}
        if get_video:
            context.update(user_video=search_video, video=get_video)
        else:
            context.update(user_video=search_video, video='')
        return render(request, 'result.html', context)


class RegisterPage(View):
    template_name = 'registration/register.html'

    def get(self, request):
        form = forms.RegForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = forms.RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()
            login(request, user)
        return redirect('/')


def logout_page(request):
    logout(request)
    return redirect('/')


def add_video(request):
    if request.method == 'POST':
        video = request.POST['video']
        AddVideo.objects.create(user=request.user.id, user_add_video=video).save()
        return redirect('/')
    return redirect(f'/video/{request.user.id}/')
