#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator, Page
from django.http import HttpResponse



def index(request):
    '''首页'''
    #查询各分类的最新4条，最热4条数据
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    context = {'title': '首页',
               'type0': type0, 'type01': type01,
               'type1': type1, 'type11': type11,
               'type2': type2, 'type21': type21,
               'type3': type3, 'type31': type31,
               'type4': type4, 'type41': type41,
               'type5': type5, 'type51': type51,
               #'cart_count': cart_count(request),
            }
    return render(request,'df_goods/index.html', context)

def list(request, tid, pindex, sort):
    '''详细列表页'''
    #根据id获取
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:3]
    goods_list = []
    if sort=='1':#默认，最新
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort=='2':#价格
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort=='3':#人气点击量
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    #创建分页
    paginator = Paginator(goods_list, 3)
    page = paginator.page(int(pindex))
    context = {'title': '商品列表',
               'ttitle': typeinfo.ttitle,
               'page': page,
               'paginator': paginator,
               'typeinfo': typeinfo,
               'sort': sort,
               'news': news,
               #'cart_count': cart_count(request),
               }
    return render(request, 'df_goods/list.html', context)

# def cart_count(request):
#     '''购物车数量，封装的一个方法查询购物车中商品数量'''
#     if request.session.has_key('user_id'):
#         return CartInfo.objects.filter(user_id=request.session['user_id'].count())
#     else:
#         return 0
