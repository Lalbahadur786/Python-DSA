def b_search_recurr(lst, low, high, x):
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == x:
        return mid
    elif lst[mid] > x:
        return b_search_recurr(lst, low, mid-1, x)
    else:
        return b_search_recurr(lst, mid+1, high, x)


lst = list(range(0, 100, 10))
print(b_search_recurr(lst, 0, len(lst)-1, 30))
