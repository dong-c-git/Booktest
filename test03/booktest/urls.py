from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$',views.index),
    #url(r'^showarg(?P<num>\d+)$',views.show_arg),   #捕获url参数，关键字参数
    #url(r'^showarg(\d+)$',views.show_arg), #捕获url参数，位置参数
    url(r'^showarg(?P<num>\d+)$', views.show_arg),# 捕获url参数:关键字参数

    url(r'^login$',views.login),  #显示登陆页面
    url(r'^login_check$',views.login_check), #登陆检查页面

    url(r'^test_ajax$',views.ajax_test),   #显示ajax页面
    url(r'^ajax_handle$',views.ajax_handle),  #ajax页面

    url(r'^login_ajax$',views.login_ajax),   #显示ajax登陆页面
    url(r'^login_ajax_check$',views.login_ajax_check),  #ajax登陆校验

    url(r'^set_cookie$',views.set_cookie),     #设置cookie
    url(r'^get_cookie$',views.get_cookie),     #获取cookie

    url(r'^set_session$',views.set_session),   #设置session
    url(r'^get_session$',views.get_session),   #获取session
    url(r'^clear_session$',views.clear_session),  #清除session
]
