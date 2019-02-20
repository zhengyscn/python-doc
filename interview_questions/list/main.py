

'''
字符串处理
字符串按空格为分隔符进行位置变动
'''
def reverseString(s):
    s_list = s.split()
    s_list.reverse()
    return ' '.join(s_list)


'''
字符串处理
通过传递的字符串和位置，进行位置变动；
'''
def shiftNum(s, n):
    kg = s.count(' ')
    idx = n % (kg + 1)

    s_list = s.split()
    res_list = s_list[idx:] + s_list[:idx]
    return ' '.join(res_list)


def main():
    s = 'hello i love beijing'
    s1 = reverseString(s)
    print(s1)

    res = shiftNum(s, 4)
    print(res)
    
    
if __name__ == '__main__':
    main()