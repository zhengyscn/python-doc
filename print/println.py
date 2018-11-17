import sys


def println(value=None, sep="\n"):
    if value:
        sys.stdout.write(value)
    sys.stdout.write(sep)
    sys.stdout.flush()  # 强制刷新 否则将阻塞

def inputln(prompt=None):
    println(prompt, sep="")
    return sys.stdin.readline() # Read until newline or EOF.

def main():
    # println()
    name = inputln("Please input your name: ")
    println(name, sep="")





if __name__ == '__main__':
    main()