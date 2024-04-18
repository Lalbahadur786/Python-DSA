def intersect_of_lists(a, b):
    i = j = 0
    m = len(a)
    n = len(b)
    res = []
    while i < m and j < n:
        if i > 0 and a[i] == a[i - 1]:
            i += 1
            continue
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1

    return res


a = [2, 4, 4, 6, 8, 9, 10]
b = [2, 3, 5, 8, 9]
b = [1, 1, 3, 3]
a = [1, 1, 1, 1, 3, 5, 7]
print(intersect_of_lists(a, b))