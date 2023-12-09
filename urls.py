"""webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hello import views


urlpatterns = [
    path("", views.index, name='home'),
    path('hello/', views.index_wrapper, name='index_wrapper'),
    path("mypage", views.mypage, name='mypage'),
    path("furnitures", views.furnitures, name="furnitures"),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
    path("mypage", views.mypage),
    path("about", views.about, name="about"),
    path(r'hello/', views.about_wrapper, name='about_wrapper'),
    path("auth", views.auth, name="auth"),
    path("index", views.index, name="index"),
    path("uslugi", views.uslugi, name="uslugi"),
]
