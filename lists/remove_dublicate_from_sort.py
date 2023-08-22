def remove_dup(lst):
    if len(lst) <= 1:
        return lst
    j = 0
    for i in range(0, len(lst)-1):
        if lst[i] != lst[i+1]:
            lst[j] = lst[i]
            j += 1
    lst[j] = lst[-1]
    return lst


lst = [10, 20, 20, 20, 30, 30, 40, 40]
print(remove_dup(lst))
