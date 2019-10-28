from django.shortcuts import render
from django.http import HttpResponse
from bookmodel.models import BookInfo
from django.template import loader,RequestContext

# Create your views here.
def my_render(request,template_path,context_dict={}):
    """使用模版文件"""
    #1、加载模版文件，模版对象
    temp = loader.get_template(template_path)
    #2、定义模版山下文，给模版文件传递数据
    context = RequestContext(request,context_dict)
    #3、渲染模版：产生标准html内容
    res_html = temp.render(context)
    #4、返回给浏览器
    return HttpResponse(res_html)

def index(request):
    return render(request,'booktest/index.html',{'content':'hello wolrd','list':list(range(1,10))})

def index2(request):
    return HttpResponse("hello python")

def show_books(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/show_books.html',{'books':books})

def detail(request,bid):
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()
    return render(request,"booktest/detail.html",{'book':book,'heros':heros})