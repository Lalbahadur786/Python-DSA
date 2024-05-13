def hoars_partition(arr, l, h):
    """
    """
    pivot = arr[l]
    i = l - 1
    j = h + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
    
def quick_sort_hoars_partition(arr, l, h):
    if h > l:
        p = hoars_partition(arr, l, h)
        quick_sort_hoars_partition(arr, l, p)
        quick_sort_hoars_partition(arr, p + 1, h)
arr = [10, 15, 1, 0, 2, 74, 56, 40, 40]
quick_sort_hoars_partition(arr, 0, 8)
print(*arr)