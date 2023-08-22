import math
# Sum of natural numbers


def sum_of_natural_num(n):
    # if num is even
    if n % 2 == 0:
        return (n//2) * (n+1)
    else:
        return ((n+1) // 2) * n


# print(f"sum of natural numbers till 6 is {sum_of_natural_num(6)}")

# Count digits in a number
def count_digits(n):
    return math.floor(math.log10(n) + 1)


# print(count_digits(104751))

# palindrome number

def palindrome_num(n):
    # Store num in temp var
    temp = n
    rev = 0
    while temp > 0:
        num = temp % 10
        rev = rev * 10 + num
        print(temp)
        temp = temp // 10
        print("temp", temp)
        print("rev", rev)
    if rev == n:
        print("palindrome")


# palindrome_num(78987)

# count trailing zeros of a factorial number
def count_fact_trail_zeros(n):
    res = 0
    divisor = 5
    while divisor <= n:
        res = res + n // divisor
        divisor *= 5
    print("Number of trailing zeros for num ", n, ":", res)


# count_fact_trail_zeros(251)

#  GCD or HCF of number
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# print(gcd(12, 15))
