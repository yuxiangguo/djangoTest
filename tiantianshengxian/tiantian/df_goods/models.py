#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    '''商品分类'''
    #标题
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=20)

class GoodsInfo(models.Model):
    '''商品类'''
    #名字
    gtitle = models.CharField(max_length=20)
    #图片
    gpic = models.ImageField(upload_to='df_goods')
    #价格
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField()
    #人气
    gclick = models.IntegerField()
    #简介
    gjianjie = models.CharField(max_length=20)
    #库存
    gkucun = models.IntegerField()
    #商品详情
    gcontent = HTMLField()
    gtype = models.ForeignKey(TypeInfo)