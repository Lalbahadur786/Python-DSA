def search(lst, x, first_start_index):
    low = 0
    high = len(lst) - 1
    answer = -1
    while (low <= high):
        mid = low + (high - low) // 2
        if lst[mid] > x:
            high = mid - 1
        elif lst[mid] < x:
            low = mid + 1
        else:
            answer = mid
            if first_start_index:
                high = mid - 1
            else:
                low = mid + 1

    return answer


def count_occurances(lst, x):
    first_index = search(lst, x, True)
    last_index = search(lst, x, False)
    return last_index - first_index + 1


lst = list((19, 20, 24, 24, 24, 30, 30, 65, 65))
print(lst)
print(count_occurances(lst, 24))
