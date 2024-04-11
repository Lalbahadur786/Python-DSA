def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        val = lst[i]
        j = i - 1
        while j >= 0 and val < lst[j]:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = val


# lst = [0, 10, 20, -1, 2, 3]
lst = [-1, -2, -3, -50, -100, -1000]
insertion_sort(lst)
print(lst)
