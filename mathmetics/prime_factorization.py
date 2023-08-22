import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i*i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Find prime factorization of a number
# For e.g n = 100 , 2 2 5 5

def prime_factors(n):
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime(i):
            while (n % i == 0):
                print(i)
                n = int(n / i)
        if n <= 1:
            break


prime_factors(315)
