from django.db import models

# Create your models here.
class BookInfoManager(models.Manager):
    """图书模型管理器类"""
    #1、改变原有查询结果集
    def all(self):
        #1、调用父类的all方法，获取所有数据
        books = super().all()
        books = books.filter(isDelete=False)
        return books

    #2、封装方法，操作模型类对应的数据表
    def create_book(self,btitle,bpub_date):
        """添加一本图书"""
        model_class = self.model
        book = model_class()
        book.btitle = btitle
        book.bpub_date = bpub_date
        #2、添加进数据库
        book.save()
        #3、返回book
        return book

#一类：
class BookInfo(models.Model):
    """图书模型类"""
    #图书名称
    btitle = models.CharField(max_length=20,db_column="title"),
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    objects = BookInfoManager()

    class Meta:
        db_table = 'bookinfo'   #指定模型类对应表名

#多类
class HeroInfo(models.Model):
    """英雄人物类"""
    #英雄名：
    hname = models.CharField(max_length=20)
    #性别
    hgender = models.BooleanField(default=False)
    #备注
    hcomment = models.CharField(max_length=200,null=True,blank=False)
    #关系属性
    hbook = models.ForeignKey('BookInfo')
    #删除标记
    isDeleta = models.BooleanField(default=False)

class AreaInfo(models.Model):
    """地区模型类"""
    #地区名称
    atitle = models.CharField(max_length=20)
    #关系属性代表当前地区的父级地区
    aParent = models.ForeignKey('self',null=True,blank=True)
