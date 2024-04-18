
def merge(arr, l, m, r):
    left = arr[l: m+1]
    right = arr[m+1: r+1]
    m = len(left)
    n = len(right)
    i = j = 0 
    k = l
    while i < m and j < n:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < m:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l+r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m , r)


arr = [-10, -5, -30, -15, -8]
merge_sort(arr, 0, 4)
print(*arr)