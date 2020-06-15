def linear_search(arr, target):
    # Your code here
    for index, value in enumerate(arr):
        if value == target:
            # print(value, index)
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    high = len(arr)
    low = 0
    # Your code here
    if len(arr) == 0:
        return -1
    while low <= high:
        # set/reset midpoint
        mid = (high + low) // 2
        # check if midpoint is target
        if arr[mid] == target:
            # return mid which equals the index
            return mid
        # check if midpoint is greater than or equal to midpoint
        if arr[mid] > target:
            # mid is the highpoint, increment by 1
            high = mid - 1
        else:
            # mid is the lowest point now and increment by 1
            low = mid + 1
    return -1  # not found