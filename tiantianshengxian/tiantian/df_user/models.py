#coding=utf-8
from __future__ import unicode_literals

from django.db import models

class UserInfo(models.Model):
    '''创建用户模型类'''
    #用户名
    uname = models.CharField(max_length = 20)
    #密码，SHA1加密为40位
    upwd = models.CharField(max_length = 40)
    #邮箱
    uemail = models.CharField(max_length = 20)
    #收货地址
    uaddress = models.CharField(max_length = 100, default = '')
    #电话
    uphone = models.CharField(max_length = 11, default = '')


class AddresseeInfo(models.Model):
    '''创建一个收件人详细信息模型类，与用户模型类位一对多关系'''
    #收件人
    aaddressee = models.CharField(max_length = 20)
    #收货地址
    aaddress = models.CharField(max_length = 100)
    #邮编
    ayoubian = models.CharField(max_length = 6)
    #电话
    aphone = models.CharField(max_length = 11)
    #关联，一对多
    auser = models.ForeignKey('UserInfo')