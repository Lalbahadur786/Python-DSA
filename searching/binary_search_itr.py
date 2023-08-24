
def b_search(lst, x):
    is_elem_found = None
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


lst = list(range(0, 100, 10))
print(lst)
print(b_search(lst, 40))
