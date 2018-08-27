import os
import json
import time

'''小文件读取'''
def readFile(FILENAME):
    try:
        fd = open(FILENAME, 'r')
        return fd.read(), True
    except Exception as e:
        return e.args, False
    finally:
        if 'fd' in locals():
            fd.close()

'''通用 写文件'''
def writeFile(FILENAME, DATA):
    try:
        fd = open(FILENAME, 'w')
        if isinstance(DATA, int):
            return fd.write(str(DATA)), True
        elif isinstance(DATA, list) or isinstance(DATA, dict):
            return fd.write(json.dumps(DATA)), True
        else:
            return "file isinstance(data) match failed.", False
    except Exception as e:
        return e.args, False
    finally:
        if 'fd' in locals():
            fd.close()

'''获取文件指针'''
def getFilePos(FILENAME):
    if not os.path.exists(FILENAME):
        os.makedirs(os.path.dirname(FILENAME))
        FILE_POS = 0
    else:
        pid, ok = readFile(FILENAME)
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
def fileStream(LOG_FILE, PID_FILE, FILE_POS):
    try:
        fd = open(LOG_FILE, 'r')
        fd.seek(FILE_POS)
        for line in fd:
            print(line, end="")
            FILE_POS += len(line)
            time.sleep(0.3)
    except KeyboardInterrupt:
        '''捕获CTRL + C'''
        msg, ok = writeFile(PID_FILE, FILE_POS)
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

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOG_FILE = os.path.join(BASE_DIR, "mysqld.log")
    PID_FILE = os.path.join(BASE_DIR, 'run', 'logstash.pid')

    FILE_POS = getFilePos(PID_FILE)
    fileStream(LOG_FILE, PID_FILE, FILE_POS)




if __name__ == '__main__':
    main()
