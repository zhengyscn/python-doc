import os
import json
import time

'''小文件读取'''
def readFile(filename):
    try:
        fd = open(filename, 'r')
        return fd.read(), True
    except Exception as e:
        return e.args, False
    finally:
        if 'fd' in locals():
            fd.close()

'''通用 写文件'''
def writeFile(filename, data):
    try:
        fd = open(filename, 'w')
        if isinstance(data, int):
            return fd.write(str(data)), True
        elif isinstance(data, list) or isinstance(data, dict):
            return fd.write(json.dumps(data)), True
        else:
            return "file isinstance(data) match failed.", False
    except Exception as e:
        return e.args, False
    finally:
        if 'fd' in locals():
            fd.close()

'''获取文件指针'''
def getFilePos(filename):
    if not os.path.exists(filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        FILE_POS = 0
    else:
        pid, ok = readFile(filename)
        if ok:
            try:
                FILE_POS = int(pid.strip())
            except:
                # warn
                FILE_POS = 0
        else:
            FILE_POS = 0
    return FILE_POS

'''流式处理'''
def fileStream(log_file, pid_file, file_pos):
    try:
        fd = open(log_file, 'r')
        fd.seek(file_pos)
        while True:
            lineinfo = fd.readline()
            print(lineinfo.strip("\n"))
            time.sleep(0.3)
            if len(lineinfo) == 0:
                break
    except KeyboardInterrupt:
        '''捕获CTRL + C'''
        msg, ok = writeFile(pid_file, fd.tell())
        if not ok:
            print(msg)
    finally:
        if 'fd' in locals():
            fd.close()

'''入口函数'''
def main():
    # print(__file__)
    # print(os.path.abspath(__file__))
    # print(os.path.dirname(os.path.abspath(__file__)))

    '''获取文件绝对路径'''
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOG_FILE = os.path.join(BASE_DIR, "mysqld.log")
    PID_FILE = os.path.join(BASE_DIR, 'run', 'logstash.pid')

    FILE_POS = getFilePos(PID_FILE)
    fileStream(LOG_FILE, PID_FILE, FILE_POS)




if __name__ == '__main__':
    main()
