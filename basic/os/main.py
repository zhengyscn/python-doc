

import os
import getpass
import socket


'''统计指定一级目录下文件、目录、软连接个数'''
def ListDir():
    rootdir = "/etc"
    ret = {'file' : {'nums' : 0, 'size'  : 0}, 'dir' : 0, 'link' : 0}
    for file in os.listdir(rootdir):
        abspath = os.path.join(rootdir, file)
        if os.path.isfile(abspath):
            ret['file']['nums'] += 1
            ret['file']['size'] += os.path.getsize(abspath)
        elif os.path.islink(abspath):
            ret['link'] += 1
        elif os.path.isdir(abspath):
            ret['dir'] += 1

    print(ret)
    return ret

'''统计指定目录下所有文件的绝对路径'''
def WalkList():
    rootdir = "/etc"
    for dirpath, dirnames, filenames in os.walk(rootdir):
        for file in filenames:
            abspath = os.path.join(dirpath, file)
            size = os.path.getsize(abspath)
            print("{:80} {:>5}k".format(abspath, size))
    '''
    for root, dirs, files in os.walk(rootdir):
        print(root, "consumes", end="")
        print(sum([os.path.getsize(os.path.join(root, name)) for name in files]), end=" ")
        print("bytes in", len(files), "non-directory files")
    '''

'''模拟Linux终端'''
def LinuxTerminal():
    while 1:
        hostname = socket.gethostname()

        # 当前登录用户
        # os.getlogin()

        current_username = getpass.getuser()
        current_uid = os.getuid()
        current_workdir = os.path.basename(os.getcwd())
        iden = '#' if current_uid == 0 else '$'

        prompt = "\033[32m[[\033[0m{}@{} {}\033[32m]]\033[0m{} ".format(current_username, hostname, current_workdir, iden)
        cmd = input(prompt)
        if cmd.startswith('rm'):
            print("\033[31mWarning, rm is disabled.\033[0m")
        else:
            os.system(cmd)

def SystemLoad():
    return os.getloadavg()


def SystemCommand():
    pass
    # os.makedirs()
    # os.rename()
    # os.rmdir()
    # os.remove()
    # os.stat()
    # os.uname()
    # os.fork()
    # os.getpgid()


def ForkChildProcess():
    '''
    Fork a child process.
    Return 0 to child process and PID of child to parent process.
    '''
    print(os.getpid(), os.getppid()) # bash
    pid = os.fork()
    if pid == 0:
        print('I am child process ({}) and my parent is {}.'.format(os.getpid(), os.getppid()))
    else:
        print('I ({}) just created a child process ({}).'.format(os.getpid(), pid))


def CurrentDir():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(BASE_DIR)


def main():
    # LinuxTerminal()

    # ListDir()

    # WalkList()

    ForkChildProcess()


if __name__ == '__main__':
    main()