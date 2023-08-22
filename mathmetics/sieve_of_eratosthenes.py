def sieve(n):
    """
    Returns the prime numbers till n
    """
    # check if less = 1
    if n <= 1:
        return
    is_prime = [True] * (n + 1)
    i = 2
    while i*i <= n:
        print("counter", i)
        if is_prime[i]:
            # print(i, end=" ")
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        i += 1
    lst = [idx for idx, num in enumerate(is_prime) if num if idx > 1]
    print("List of prime numbers:", lst)


sieve(23)
