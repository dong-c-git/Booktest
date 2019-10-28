from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from booktest.models import BookInfo
from datetime import datetime,timedelta


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

#/login_ajax
def login_ajax(request):
    """显示登陆页面"""
    return render(request,'booktest/login_ajax.html')

#/login_ajax_check
def login_ajax_check(request):
    """ajax登陆校验"""
    #1、获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    #2、进行校验，返回json数据
    if username == 'smart' and password == '123':
        #用户名密码正确
        return JsonResponse({'res':1})
        #return redirect('/index') ajax请求在后台，不用返回页面或重定向
    else:
        #用户名或密码错误
        return JsonResponse({'res':0})

#/set_ccokies
def set_cookie(request):
    """设置cookie信息"""
    response = HttpResponse("设置cookie")
    #设置一个cookie信息，名字为num,值为1
    response.set_cookie('num',1,max_age=14*24*3600)
    response.set_cookie('num2',2)
    response.set_cookie('num',1,expires=datetime.now()+timedelta(days=14))
    #返回response
    return response

#/get_cookie
def get_cookie(request):
    """获取cookie信息"""
    #取出cookie num的值
    num = request.COOKIES['num']
    return HttpResponse(num)

#/set_session
def set_session(request):
    """设置session"""
    request.session['username'] = 'smart'
    request.session['age'] = 18
    #设置session有效期
    #request.session.set_expiry(5)
    return HttpResponse('设置session')

#/get_session
def get_session(request):
    """获取session"""
    username = request.session['username']   #session不存在会报异常
    age = request.session['age']
    return HttpResponse(username+':'+str(age))

#/clear_session
def clear_session(request):
    """清除session信息"""
    #request.session.clear()
    request.session.flush()
    return HttpResponse("清除成功")