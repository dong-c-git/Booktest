from django.contrib import admin
from bookmodel.models import BookInfo,HeroInfo
# # Register your models here.
#后台管理相关文件
#自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ["id","btitle","bpub_date"]

class HeroInfoAdmin(admin.ModelAdmin):
    """英雄人物模型管理类"""
    list_display = ["id","hname","hcontent"]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)