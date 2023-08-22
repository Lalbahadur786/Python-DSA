import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n))+1, 2):
        print("hi", i)
        if n % i == 0:
            return False
    return True


print(is_prime(79))
