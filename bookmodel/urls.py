"""Booktest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from bookmodel import views


urlpatterns = [
    #通过url函数设置url路由配置项
    url(r'^index$',views.index),  #建立/index和视图index之间的关系
    url(r'^index2',views.index2),
    url(r'^books$',views.show_books), #显示图书信息
    url(r'^books/(\d+)$',views.detail),#显示英雄信息
]
