def comp_pow(i, n):
    temp = 0
    if n == 0:
        return 1
    temp = comp_pow(i, n // 2)
    if n % 2 == 0:
        return temp * temp
    else:
        return i * temp * temp


print(comp_pow(2, 5))
