from math import inf


def merge(a: list, p, q, r):
    left, right = a[p:q + 1], a[q + 1:r + 1]
    left.append(inf)
    right.append(inf)
    s = t = 0
    for u in range(p, r + 1):
        if left[s] <= right[t]:
            a[u] = left[s]
            s += 1
        else:
            a[u] = right[t]
            t += 1

def merge_sort(array, i, j):
    if i < j:
        k = (i + j) // 2
        merge_sort(array, i, k)
        merge_sort(array, k + 1, j)
        merge(array, i, k, j)
