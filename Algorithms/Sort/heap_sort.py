def trickle_down(array, i):
    heap_size, left_child = len(array) - 1, 2*i + 1
    largest = left_child if left_child <= heap_size and array[left_child] > array[i] else i
    right_child = left_child + 1
    if right_child <= heap_size and array[right_child] > array[largest]:
        largest = right_child
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        trickle_down(array, largest)


def build_max_heap(array):
    for i in range((len(array) - 1) // 2, -1, -1):
        trickle_down(array, i)

a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
build_max_heap(a)
print(a)
