
def insertion_sort(lst):
    #take first element as sorted subarray
    # then get an element from the remaining list and place in subarray
    for i in range(len(lst)):
        j = i - 1
        val = lst[i]
        while j >= 0 and lst[j] > val:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = val
    return lst
        




lst = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
print(insertion_sort(lst))