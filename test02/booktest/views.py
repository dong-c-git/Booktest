from django.shortcuts import render,redirect
from booktest.models import BookInfo,AreaInfo
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    """显示图书信息"""
    #1、查询出所有图书的信息
    books = BookInfo.objects.all()
    print(books)
    #2、使用模版
    return render(request,'booktest/index.html',{'books':books})

def create(request):
    """新增一本图书"""
    #1、创建bookinfo对象
    b = BookInfo()
    #b.title = '流星蝴蝶剑'
    b.bpub_date = date(1990,1,1)
    b.bread = 32
    b.bcomment = 45
    b.isDelete = 0
    b.save()
    return HttpResponse("ok")

def delete(request,id):
    """删除一本图书"""
    b = BookInfo.objects.get(id=id)
    b.delete()
    return redirect('/index')