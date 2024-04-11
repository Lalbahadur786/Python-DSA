def merge_two_lists(lst1, lst2):
    m = len(lst1)
    n = len(lst2)
    i = 0
    j = 0
    res_lst = []
    while i < m and j < n:
        if lst1[i] < lst2[j]:
            res_lst.append(lst1[i])
            i += 1
        else:
            res_lst.append(lst2[j])
            j += 1
    while i < m:
        res_lst.append(lst1[i])
        i += 1
    while j < n:
        res_lst.append(lst2[j])
        j += 1
    return res_lst


lst1 = [2, 10, 11, 15, 20, 30]
lst2 = [1, 8, 13, 14, 20, 25]
print(merge_two_lists(lst2, lst1))
