def count_1s(lst, low, high):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    # For increasing order array
    # if lst[mid] == 1:
    #     if mid == 0 or lst[mid-1] != lst[mid]:  # for in creasing order lst
    #         return mid
    #     else:
    #         return count_1s(lst, low, mid - 1)

    # return count_1s(lst, mid+1, high)

    # for decreasing ordered array
    if lst[mid] == 0:
        # for in creasing order lst
        if mid == 0 or lst[mid-1] != lst[mid]:
            return mid
        else:
            return count_1s(lst, low, mid-1)
    return count_1s(lst, mid+1, high)


lst_d = list((1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0))
lst_i = list((0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1))
# print(len(lst_i)-count_1s(lst_i, 0, len(lst_i)-1))
print(count_1s(lst_d, 0, len(lst_d)-1))
