
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    c=[]
    a_index, b_index = 0, 0
    while a_index < len(arrA) and b_index < len(arrB):
        if arrA[a_index] < arrB[b_index]:
            c.append(arrA[a_index])
            a_index += 1
        else:
            c.append(arrB[b_index])
            b_index += 1
    if a_index == len(arrA): 
        c.extend(arrB[b_index:])
    else:
        c.extend(arrA[a_index:])
    # print(c)
    return c


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1: 
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
