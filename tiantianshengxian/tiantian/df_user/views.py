#coding=utf-8
from django.shortcuts import render, redirect
from models import *
from hashlib import sha1
from django.http import JsonResponse,HttpResponseRedirect

def register(request):
    '''定义注册页面视图'''
    return render(request, 'df_user/register.html')

def register_handle(request):
    '''定义注册页面'''
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

def register_exist(request):
    '''判断用户名是否已经存在'''
    uname = request.GET.get('uname')
    #判断uname是否存在，count方法，要么返回1，要么返回零
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    '''定义登录页面'''
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request, 'df_user/login.html',context)

def login_handle(request):
    '''接受用户登录的请求信息'''
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    #是否记住用户名，默认为记住1，如果不勾选赋值为0
    jizhu = post.get('jizhu', 0)
    #根据用户名查询对象
    user = UserInfo.objects.filter(uname=uname)
    if len(user)==1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest()==user[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            #记住用户名
            if jizhu!=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookies('uname', '', max_length=-1)
            request.session['user_id'] = user[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title':'用户名登录', 'error_name':0, 'error_pwd':1, 'uname':uname, 'upwd':upwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title':'用户登录', 'error_name':1, 'error_pwd':1, 'uname':uname, 'upwd':upwd}
        return render(request, 'df_user/login.html', context)