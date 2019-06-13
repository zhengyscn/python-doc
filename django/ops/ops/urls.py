"""ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from hello.views import hello, SumInputViewV1, CommandViewV1
from hello.views import SumInputViewV2, CommandViewV2
from hello.views import LoginPageView, loginCheckView
from users.views import UserLoginView, UserLogoutView, UserListView, UserCreateView, UserDeleteView, UserUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # hello world
    url(r'^hello/$', hello),

    # url 求和
    url(r'^hello/v1/input_sum/$', SumInputViewV1),
    url(r'^hello/v1/command/$', CommandViewV1),

    # 页面操作
    url(r'^hello/v2/input_sum/$', SumInputViewV2),
    url(r'^hello/v2/command/$', CommandViewV2),

    # login page
    url(r'^hello/login/$', LoginPageView),
    url(r'^hello/login_check/$', loginCheckView),

    # login
    url(r'^user/login/', UserLoginView),
    url(r'^user/logout/', UserLogoutView),

    # add delete udpate list
    url(r'^user/add/', UserCreateView),
    url(r'^user/delete/(?P<pk>\d+)', UserDeleteView),
    url(r'^user/update/(?P<pk>\d+)', UserUpdateView),
    url(r'^users/list/', UserListView),

]
