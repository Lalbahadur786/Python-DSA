def first_occur_itr(lst, low, high, x):
    low = 0
    high = len(lst) - 1
    while (low <= high):
        mid = low + (high - low) // 2
        if x < lst[mid]:
            high = mid - 1
        elif x > lst[mid]:
            low = mid + 1
        elif mid == 0 or lst[mid - 1] != lst[mid]:
            # elif lst[mid] == x:
            return mid
        else:
            high = mid - 1
    return -1


lst = list((10, 20, 24, 24, 30, 30, 65, 65))
print(lst)
low = 0
high = len(lst) - 1
print(first_occur_itr(lst, low, high, 241))
