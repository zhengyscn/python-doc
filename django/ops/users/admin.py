from django.contrib import admin

# Register your models here.
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    # https://www.cnblogs.com/wumingxiaoyao/p/6928297.html

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['username', 'age', 'phone', 'address', 'create_time', 'update_time']

    # 搜索字段
    search_fields = ['username', 'phone']

    # 过滤字段
    list_filter = ['username', 'phone']

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ['-update_time', 'create_time']

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 2

    # list_editable 设置默认可编辑字段
    # list_editable = ['machine_room_id', 'temperature']


admin.site.register(Users, UsersAdmin)
