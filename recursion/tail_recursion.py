def fact_tail(n, res):
    if n <= 0:
        return res
    return fact_tail(n-1, res*n)


print(fact_tail(5, 1))
