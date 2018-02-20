from  django.contrib import admin
from models import *

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_diaplay = ['id', 'gtitle', 'gpic', 'gprice', 'isDelete',
                    'gunit', 'glick', 'gjianjie', 'gkucun',
                    'gcontent', 'gtype']


admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)