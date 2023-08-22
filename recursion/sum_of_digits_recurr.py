def sum_of_digits(n):
    if n < 10:
        return n
    return sum_of_digits(n//10) + n % 10


print(sum_of_digits(253))
