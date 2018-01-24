#coding=utf-8
from django.shortcuts import render, redirect
from models import *
from hashlib import sha1

def register(request):
    '''定义注册页面视图'''
    return render(request, 'df_user/register.html')

def register_handle(request):
    '''定义点击注册后转向页面'''
    #接受用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')
    #判断两次密码是否相等
    if upwd != ucpwd:
        #重定向页面
        return redirect('/user/register/')
    #密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd1 = s1.hexdigest()
    #创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd1
    user.uemail = uemail
    # 别忘了save否则无法上传到数据库
    user.save()
    #注册成功，转到登录页
    return redirect('/user/login/')