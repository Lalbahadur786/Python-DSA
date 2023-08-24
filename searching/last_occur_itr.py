def last_occur_itr(lst, x):
    low = 0
    high = len(lst) - 1
    count_occur = 0
    while (low <= high):
        mid = low + (high - low) // 2
        if lst[mid] > x:
            high = mid - 1
        elif lst[mid] < x:
            low = mid + 1
        elif mid == (len(lst) - 1) or lst[mid + 1] != lst[mid]:
            return mid
        else:
            low = mid + 1
    return -1


lst = list((10, 20, 24, 24, 30, 30, 65, 65))
print(lst)
print(last_occur_itr(lst, 65))
