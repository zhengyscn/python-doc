
'''快拍排序'''
def quick_sort(arr):
    print(arr)
    input()
    if len(arr) <= 1:
        return arr
    left = []
    right = []
    start = arr[0]
    for x in arr[1:]:
        if x < start:
            left.append(x)
        else:
            right.append(x)
    print("---->left>>>>", left)
    print("---->right>>>", right)
    return quick_sort(left) + [start] + quick_sort(right)

def main():
    import random
    arr = [ random.randint(1, 100) for x in range(1, 11)]
    print("Before arr {}".format(arr))
    arr = quick_sort(arr)
    print("After arr {}".format(arr))


if __name__ == '__main__':
    main()
