

# 标准模块
import os
import sys

# 第三方模块
from prettytable import PrettyTable
from jinja2 import Environment, FileSystemLoader


def load():
    '''
    加载文件数据到内存
    :return: dict
    '''
    pass

def dump():
    '''
    写内存数据到文件中
    :return:
    '''
    pass

def addUser():
    '''
    添加用户
    add monkey 12 132xxx beijing
    :return:
    '''
    pass

def updateUser():
    '''
    修改用户
    update monkey set age = 20
    :return:
    '''
    pass

def deleteUser():
    '''
    删除用户
    delete monkey
    :return:
    '''
    pass

def listUser():
    '''
    列出全部用户
    list
    :return:
    '''
    pass

def findUser():
    '''
    查找指定用户
    find monkey
    :return:
    '''
    pass

def logout():
    '''
    退出
    exit
    :return:
    '''
    pass

def displayUser():
    '''
    分页
    :return:
    display page 2
    display page 2 pagesize 5
    '''
    pass

def outputHtml():
    '''
    输出html
    html
    :return:
    '''
    # https://www.programcreek.com/python/example/1632/jinja2.Environment
    # 配置jinja2在本地文件系统的搜索路径
    loader = FileSystemLoader('.', followlinks=True)
    env = Environment(loader=loader)
    template = env.get_template('index.html')
    data = template.render(object_list={})
    print(data)


def main():
    '''
    入口函数
    :return:
    '''
    pass

    outputHtml()


if __name__ == '__main__':
    main()