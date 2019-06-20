from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Teacher, Course, Student, TeacherAssistant

class TeacherAdmin(admin.ModelAdmin):

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['username', 'intro', 'create_at', 'update_at']

    # 搜索字段
    search_fields = ['username',]

    # 过滤字段
    list_filter = ['create_at', ]

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ['-update_at', 'create_at']

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10



class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'create_at', 'update_at']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'age', 'sex', 'update_at']

class TeacherAssistantAdmin(admin.ModelAdmin):
    list_display = ['username', 'love', 'update_at']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(TeacherAssistant, TeacherAssistantAdmin)

