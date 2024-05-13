def naive_partition_scheme(a):
    p = 30
    temp = []
    # search of this partition mid element
    # and move it to the end so that order of elements can be maintained
    p_i = a.index(p)
    a[p_i], a[-1] = a[-1], a[p_i]
    print(a)
    for num in a[:-1]:
        if num <= p:
            temp.append(num)
    temp.append(p)
    for num in a[:-1]:
        if num > p:
            temp.append(num)
    return temp


a = [12, 15, 48, 50, 36, 30, 14]
print(naive_partition_scheme(a))