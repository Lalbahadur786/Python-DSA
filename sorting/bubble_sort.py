def bubble_sort(lst):
    n = len(lst)
    for i in range(0, n-1):
        print("pass:", i)
        is_swapped = False
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                is_swapped = True
        if not is_swapped:
            break


lst = [41, 2, 4, 50, 60, 74, 45]
print("before, swapping", lst)
bubble_sort(lst)
print(lst)
