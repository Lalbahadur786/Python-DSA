def partition(arr_num, low, high):
    i = low -1
    pivot = arr_num[high]
    for j in range(low, high):
        if arr_num[j] <= pivot:
            print(arr_num[j], pivot)
            i = i + 1
            (arr_num[i], arr_num[j]) = (arr_num[j], arr_num[i])
    (arr_num[i+1], arr_num[high]) = (arr_num[high], arr_num[i+1])
    print(arr_num)
    return i + 1

def quick_sort(arr_num, low, high):
    if low < high:
        print("low-high")
        print(low, high)
        print("Partition called")
        pi = partition(arr_num, low, high)
        print("value of pi is", pi)
        print("")
        quick_sort(arr_num, low, pi-1)
        quick_sort(arr_num, pi+1, high)

# Driver code
arr_num = [9,8,7,6,5,4,3,2,1]
arr_num1 = [10,60,50,20,40,30]
quick_sort(arr_num1,0,len(arr_num1)-1)
print(arr_num1)