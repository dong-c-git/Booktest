from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from booktest.models import BookInfo


# Create your views here.

def index(request):
    """首页处理函数"""
    response = render(request,'booktest/index.html')
    response.write('hello')
    return response

def show_arg(request,num):
    return HttpResponse(num)

def login(request):
    """显示登陆页面"""
    #判断用户是否登陆
    if request.session.has_key('islogin'):
        print(request.session)
        #用户已经登陆，跳转到首页
        return redirect('/index')
    else:
        #用户未登陆
        if 'username' in request.COOKIES:
            #获取记住到用户名
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request,'booktest/login.html',{'username':username})

def login_check(request):
    """登陆校验视图"""
    print(request.method)
    #1、获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    #2、进行登陆校验
    #实际开发：根据用户名和密码查找数据库
    #模式：smart 123
    print(username,password)
    if username == 'smart' and password == '123':
        #用户名密码正确，跳转到首页
        response = redirect('/index')
        #判断是否需要记住用户名
        if remember == 'on':
            #设置cookie username,过期时间一周
            response.set_cookie('username', username, max_age=7*24*3600)
        #记住用户登陆状态
        #只有session中有islogin,就认为用户已经登陆
        request.session['islogin']= True
        print(request.session)
        #返回应答
        return response
    else:
        #用户名或密码错误，跳转到登陆页面
        return redirect('/login')

#/test_ajax
def ajax_test(request):
    """显示ajax页面"""
    return render(request,'booktest/test_ajax.html')

def ajax_handle(request):
    """ajax请求处理"""
    #返回json数据
    return JsonResponse({'res':1})