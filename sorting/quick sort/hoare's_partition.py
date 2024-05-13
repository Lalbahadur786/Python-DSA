def hoars_partition(a, l, h):
    pivot = a[l]
    i = l - 1
    j = h + l
    while True:

        # move right i for less than pivot elem
        i += 1
        while a[i] < pivot:
            i += 1

        # move left j for greater than pivot elem
        j -= 1
        while a[j] > pivot:
            j -= 1
        
        # return 
        if i >= j:
            return j
        
        # swap elements
        a[i], a[j] = a[j], a[i]

a = [30, 1, 5, 7, 8, 10, 47, 15, 30]

print(hoars_partition(a, 0, 8))
print(a)