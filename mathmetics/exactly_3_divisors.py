import time
import math


def exact_3_div(n):
    dict1 = {}
    t1 = time.time()
    for i in range(n):
        dict1[i] = [1]
        for j in range(2, i+1):
            if i % j == 0:
                dict1[i].append(j)
    t2 = time.time()
    return [dict1, (t2-t1)]


# print(exact_3_div(10000))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def exact_3_div_opt(n):
    t1 = time.time()
    exact_3_divisors = 0
    for j in range(2, n):
        if (j*j) > n:
            num = j - 1
            break
    for i in range(2, num+1):
        if is_prime(i):
            if (i * i) <= n:
                exact_3_divisors += 1
    t2 = time.time()
    return [exact_3_divisors, (t2 - t1)]


print("optimized", exact_3_div_opt(1000000))
