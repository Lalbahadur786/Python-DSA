import math


def all_divisior_of_num(n):
    """
    """
    i = 1
    while (i * i < n):
        if n % i == 0:
            print(i)
        i += 1
    while (i >= 1):
        if n % i == 0:
            print(int(n / i))
        i -= 1


all_divisior_of_num(100)
