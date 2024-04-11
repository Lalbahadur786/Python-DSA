def selection_sort(lst):
    for i in range(0, len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


lst = [50, 10, 40, 30, 45, 10, -1]
selection_sort(lst)
print(lst)
