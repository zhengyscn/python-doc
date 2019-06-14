from django.shortcuts import render

# Create your views here.
import csv
import datetime

from .models import Users

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET','POST'])
def UserLoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '51reboot' and password == '123456':
            return redirect('/users/list/')
    else:
        return render(request, 'user_login.html')

@require_http_methods(['GET'])
def UserLogoutView(request):
    return redirect("/user/login/")

@require_http_methods(['GET','POST'])
def UserCreateView(request):

    if request.method == 'GET':
        return render(request, 'user_add.html')

    elif request.method == 'POST':
        data = request.POST.dict()
        try:
            Users.objects.create(**data)
        except Exception as e:
            errMsg = "Create user err, msg: {}".format(e.args)
            print(errMsg)
            context = {'code' : -1, 'msg' : errMsg}
            return render(request, 'user_add.html', context=context)
        return redirect('/users/list/')

@require_http_methods(['GET'])
def UserListView(request):

    if request.method == 'GET':
        objs = Users.objects.all()
        return render(request, 'users.html', context={'object_list' : objs})

@require_http_methods(['GET'])
def UserDeleteView(request, pk):

    if request.method == 'GET':
        context = {'code': -1, 'data' : '', 'msg': ''}

        try:
            obj = Users.objects.get(pk=pk)
        except Exception as e:
            errMsg = "Get user err, msg: {}".format(e.args)
            context['msg'] = errMsg
        else:
            obj.delete()
            context['msg'] = "Delete succ"
        return redirect("/users/list/")

@require_http_methods(['GET','POST'])
def UserUpdateView(request, pk):

    if request.method == 'GET':
        obj = Users.objects.get(pk=pk)
        return render(request, 'user_update.html', context={'obj' : obj})

    elif request.method == 'POST':
        data = request.POST.dict()
        data.pop("username", None)
        Users.objects.filter(pk=pk).update(**data)
        return redirect("/users/list/")



'''导出csv
'''
@require_http_methods(['GET'])
def UserExportCsvView(request):
    # Create the HttpResponse object with the appropriate CSV header.
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="51reboot-{}.csv"'.format(cur_time)

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response