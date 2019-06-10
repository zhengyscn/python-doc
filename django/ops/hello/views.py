from django.shortcuts import render

# Create your views here.
import json
import shlex
import subprocess

from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate


def hello(request):
    print("request: ", request)
    print("dir(request): ", dir(request))
    return HttpResponse("hello world.")


def helloJson(request):
    dic = {
        'name' : '51reboot',
        'address' : 'beijing',
    }
    content = json.dump(dic)
    return HttpResponse(content, content_type="application/json")
    # return JsonResponse(dic)


def helloDic(request):
    dic = list(range(10))
    return JsonResponse(dic, safe=False)


def CommandView(request):
    cmd = request.GET.get('cmd', None)
    if cmd:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        return HttpResponse(stdout, content_type="text/plain")
    else:
        return HttpResponse("cmd args is required.")


def loginCheckView(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    if not username or not password:
        return HttpResponse("username or password args is required.")

    if username == '51reboot' and password == '123456':
        return HttpResponse('Login ok')
    else:
        return HttpResponse('Valid failed.')


def LoginPageView(request):
    htmlStr = '''
    <html>
    <body>
        <form action="#" method="get">
            Username: <input type="text" name="username"><br/>
            Password: <input type="text" name="password"><br/>
            <input type="submit" value="Submit">
        </form>
        <a href="/input">重置url</a>
    </body>
    </html>
    '''
    return HttpResponse(htmlStr)


def SumInputViewV1(request):
    '''
    /?n1=2&n2=3
    <QueryDict: {'n1': ['2'], 'n2': ['3']}>

    /?n1=2&n2=3&n1=100
    < QueryDict: {'n1': ['2', '100'], 'n2': ['3']} >
    '''
    if request.method == "GET":
        print(request.GET)
        '''
        request.GET['n1'] = 200  # 验证是否可修改字典
        
        data = request.GET.copy()
        data['n1'] = 200
        '''
        x = request.GET.get("x")
        print("x: {}".format(x))

        x1 = request.GET.getlist("x")
        print("x1: {}".format(x1))

        y = request.GET.get("y")
        print("y: {}".format(y))

        s = int(x) + int(y)
        result = "{} + {} = {}".format(x, y, s)
        return HttpResponse(result)

    elif request.method == "POST":
        print(request.POST)
    return HttpResponse("hello world.")

def CommandViewV1(request):
    cmdArgs = request.GET.get('cmd')
    cmd = shlex.split(cmdArgs)

    # p = subprocess.Popen(["df"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if stderr:
        return HttpResponse(stderr)
    else:
        return HttpResponse(stdout)

def SumInputViewV2(request):
    pass

def CommandViewV2(request):
    pass

def LoginTemplateView(request):
    return render(request, "login.html", context={"username" : "monkey"})

def cus_user_login(request):
    '''
    1. 获取用户提交的用户名和密码
    2. 根据用户名从数据库里取出这条记录
    3. 不存在
    4. 存在, 判断密码是否一致.
    '''
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            obj = User.objects.get(username=username)
        except Exception as e:
            print(e.args)
            return e.args, False

        check_ok = obj.check_password(password)
        if check_ok:    # 验证成功
            pass
        else:           # 验证失败
            pass
        return JsonResponse()

def user_login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print("login succ.")
            return HttpResponse("login succ")
        else:
            pass
            print("login fail.")
            return HttpResponse("login fail")
    else:
        return HttpResponse("request method invalid.")

