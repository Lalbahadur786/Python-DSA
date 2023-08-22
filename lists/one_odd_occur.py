def one_odd_occur(a):
    res = 0
    for i in a:
        res = res ^ i
    return res


a = [1, 1, 2, 2, 3, 3, 4, 4, 4]
print(one_odd_occur(a))
