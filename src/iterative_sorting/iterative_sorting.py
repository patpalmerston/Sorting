# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        if smallest_index != i:
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]


        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    arr_length = len(arr) -1
    arr_state = False

    while not arr_state:
        arr_state = True
        for i in range(0, arr_length):
            if arr[i] > arr[i+1]:
                arr_state = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr