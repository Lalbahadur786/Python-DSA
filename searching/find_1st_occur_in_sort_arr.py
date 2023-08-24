def first_occurance(lst, low, high, x):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if x > lst[mid]:
        return first_occurance(lst, mid+1, high, x)
    elif x < lst[mid]:
        return first_occurance(lst, low, mid - 1, x)
    elif mid == 0 or lst[mid - 1] != lst[mid]:
        return mid
    else:
        return first_occurance(lst, low, mid-1, x)


lst = list((10, 20, 24, 24, 30, 30, 65, 65))
print(lst)
low = 0
high = len(lst) - 1
print(first_occurance(lst, low, high, 24))
