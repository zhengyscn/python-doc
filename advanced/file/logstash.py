import os
import time


def readFile(filename):
    try:
        fd = open(filename, 'r')
        return fd.read(), True
    except Exception as e:
        return e.args, False
    finally:
        if 'fd' in locals():
            fd.close()


def writeFile(filename, data):
    try:
        fd = open(filename, 'w')
        if isinstance(data, int):
            return fd.write(str(data)), True
        elif isinstance(data, list):
            pass
    except Exception as e:
        return e.args, False
    finally:
        if 'fd' in locals():
            fd.close()


def getFilePos(filename):
    if not os.path.exists(filename):
        FILE_POS = 0
    else:
        pid, ok = readFile(filename)
        if ok:
            FILE_POS = int(pid.strip())
        else:
            FILE_POS = 0
    return FILE_POS


def fileStream(LOG_FILE, PID_FILE, FILE_POS):
    try:
        fd = open(LOG_FILE, 'r')
        fd.seek(FILE_POS)
        for line in fd:
            print(line, end="")
            FILE_POS += len(line)
            time.sleep(0.3)
    except KeyboardInterrupt:
        '''CTRL + C'''
        msg, ok = writeFile(PID_FILE, FILE_POS)
        if not ok:
            print(msg)
    finally:
        if 'fd' in locals():
            fd.close()


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
