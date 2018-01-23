#coding=utf-8
from django.shortcuts import render

def register(request):
    '''定义注册页面视图'''
    return render(request, 'df_user/register.html')
