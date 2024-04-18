
def sort_subarray(lst, low, high, mid):
    left = lst[low: mid+1]
    right = lst[mid+1:high+1]
    m = len(left)
    n = len(right)
    i = j = 0
    k = low
    while i < m and j < n:
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
            k += 1
        else:
            lst[k] = right[j]
            j += 1
            k += 1
    while i < m:
        lst[k] = left[i]
        i += 1
        k += 1

    while j < n:
        lst[k] = right[j]
        j += 1
        k += 1
    return lst


big_lst = [10, 15, 20, 40, 2, 3, 50]
low = 0
high = 6
mid = 3
print(sort_subarray(big_lst, low, high, mid))
