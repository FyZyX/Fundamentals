def binary_search(array, target):
    low, high = 0, len(array)
    while low + 1 < high:
        middle = (low + high) // 2
        if array[middle] > target:
            high = middle
        else:
            low = middle
    if array[low] == target:
        return low
    else:
        return -1
