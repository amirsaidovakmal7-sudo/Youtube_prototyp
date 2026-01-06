from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>', views.category_page),
    path('video/<int:pk>', views.video_page),
    path('search', views.search),
    path('register', views.RegisterPage.as_view()),
    path('logout', views.logout_page),
    path('add-video-to-form', views.add_video),
]