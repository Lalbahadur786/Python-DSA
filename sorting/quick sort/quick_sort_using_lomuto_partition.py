def lomuto_partition(arr, l, h):
    """
    """
    i = l - 1
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            # swapping the numbers less than equal to pivot
            arr[i], arr[j] = arr[j], arr[i]
    # swap partition element to its correct position
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i + 1

def quick_sort_lomuto(arr, l, h):
    if h > l:
        p = lomuto_partition(arr, l, h)
        quick_sort_lomuto(arr, l, p - 1)
        quick_sort_lomuto(arr, p + 1, h)

arr = [4, 5, 10, 1, 2, 74, 50, 8]
arr = [10, 15, 1, 0, 2, 74, 56, 40, 40]
quick_sort_lomuto(arr, 0, len(arr)-1)
print(*arr)