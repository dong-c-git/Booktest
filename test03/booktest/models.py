from django.db import models

# Create your models here.
class BookInfo(models.Model):
    #btitle = models.CharFiled(max_length=20)
    btitle = models.CharField(max_length=20)

