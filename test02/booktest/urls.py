from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index/$',views.index),  #图书信息页面
    url(r'^create$',views.create), #新增图书案例
    url(r'^delete(\d+)$',views.delete),#删除一本图书
]
