from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    # for better organisation you have to name it by his package, in place of just home we name it blog-home
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"), 
]