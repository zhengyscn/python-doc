from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from .models import Teacher, Course, Student, TeacherAssistant


def SchoolView(request, *args, **kwargs):
    # 返回新QuerySet API
    # .all() .filter() .order_by() .exclude() .distinct()

    # 实现一些字段别名，选择/过滤一些字段
    # .extra() .defer() .only()


    return HttpResponse("ok.")