import sys
import signal


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

# register func handler
'''
signal.SIGINT

SIGINT    终止进程  中断进程  (control+c)
SIGTERM   终止进程     软件终止信号
SIGKILL   终止进程     杀死进程
SIGALRM   闹钟信号
'''
signal.signal(signal.SIGINT, signal_handler)

# Wait until a signal arrives.
# 阻塞调用
signal.pause()