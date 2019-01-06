
'''冒泡排序'''
def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            # print(i, j)
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]



def main():
    import random
    arr = [ random.randint(1, 100) for x in range(1, 11)]
    print("Before arr {}".format(arr))
    bubble_sort(arr)
    print("After arr {}".format(arr))


if __name__ == '__main__':
    main()
