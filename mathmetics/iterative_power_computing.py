def iter_pow_cpmpute(x, y):
    temp = 1
    while y > 0:
        if y % 2 != 0:
            print("1", end=" ")
            temp *= x
        else:
            print("0", end=" ")
        x = x * x
        y = y // 2
    print(temp)


iter_pow_cpmpute(2, 5)
