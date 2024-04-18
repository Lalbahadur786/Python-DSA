def merge(a, l, mid, r):
    left = a[l: mid+1]
    right = a[mid+1: r+1]
    m = len(left)
    n = len(right)
    i = j = 0
    k = l
    res = 0
    while i < m and j < n:
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
            k += 1
        else:
            a[k] = right[j]
            res += len(left) - i
            j += 1
            k += 1
    while i < m:
        a[k] = left[i]
        i += 1
        k += 1
    while j < n:
        a[k] = right[j]
        j += 1
        k += 1
    return res
def merge_sort(a, l, r):
    res = 0
    if r > l:
        m = (l + r ) // 2
        res += merge_sort(a, l, m)
        res += merge_sort(a, m+1, r)
        res += merge(a, l, m, r)
    return res

a = [2, 4, 1, 3, 5]
a = [10, 5, 30, 15, 7]
print(merge_sort(a, 0, 4))
print(*a)
