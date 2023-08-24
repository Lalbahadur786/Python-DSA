def last_occur(lst, low, high, x):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if lst[mid] < x:
        return last_occur(lst, mid+1, high, x)
    elif lst[mid] > x:
        return last_occur(lst, low, mid-1, x)
    elif mid == (len(lst) - 1) or lst[mid+1] != lst[mid]:
        return mid
    else:
        return last_occur(lst, mid+1, high, x)


lst = list((10, 20, 24, 24, 30, 30, 65, 65))
print(lst)
low = 0
high = len(lst) - 1
print(last_occur(lst, low, high, 65))
