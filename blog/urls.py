from django.urls import path
from . import views

urlpatterns = [

    path('home/',views.home, name="home"),
    path('blog/',views.blogging,name="blog"),
    path('post/',views.blogs,name="post")

]