import os
import datetime

'''
通过os模块实现一个需求
1. 在当前用户的家目录下写一个文件cd.py
2. 获取当前路径并打印当前路径；
3. 切换到/tmp/<当前日期>/， 没有没有此文件， 要求创建此目录， 通过python的方式创建
4. 
'''

FILE_DB = '51reboot.db'

datedir = datetime.datetime.now().strftime("%Y%m%d")

CURRENT_DIR = os.getcwd()
# print(CURRENT_DIR)

workdir = os.path.join("/tmp", datedir)
# print(workdir)

try:
    os.chdir(workdir)
except FileNotFoundError:
    os.mkdir(workdir)
    os.chdir(workdir)

# 打开文件
fd = os.open(FILE_DB, os.O_RDWR|os.O_CREAT) # 返回新打开文件的描述符。

# 写入数据
os.write(fd, "monkey".encode()) # to bytes

# 关闭文件
os.close(fd)

os.chmod(os.path.join(workdir, FILE_DB), 0o644) # python3 o

os.chown(os.path.join(workdir, FILE_DB), 501, 27)


CURRENT_DIR = os.getcwd()
print(CURRENT_DIR)

