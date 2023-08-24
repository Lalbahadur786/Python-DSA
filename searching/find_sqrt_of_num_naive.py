def find_sqrt_naive(x):
    i = 1
    while i * i <= x:
        i += 1
    return i - 1


# print(find_sqrt_naive(25))

# using binary serach method

def find_sqrt_b_search(x):
    low = 1
    high = x
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        mid_sq = mid * mid
        if mid_sq == x:
            return mid
        elif mid_sq > x:
            high = mid - 1
        else:
            low = mid + 1
            ans = mid
    return ans


print(find_sqrt_b_search(10))
