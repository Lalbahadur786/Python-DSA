# Bubble sort  in first full pass you largest number would be at end
def bubble_sort(arr_num):
    for i in range(0, len(arr_num)-1):
        print(f"pass ->{i}")
        is_swapped = False
        for j in range(0, len(arr_num)-1):
            if arr_num[j] > arr_num[j+1]:
                arr_num[j+1], arr_num[j] = arr_num[j], arr_num[j+1]
                is_swapped = True
                print(f"arr_content: {arr_num}")
        if not is_swapped:
            print("breaking the main loop due to no more swaps")
            break
    return arr_num


# insertion sort    will created sorted-unsorted sub array
def  insertion_sort(arr_num):
    for i in range(1,len(arr_num)):
        key = arr_num[i]
        for j in range(i):
            if arr_num[j] > key:
                del arr_num[i]
                arr_num[j], arr_num[j+1:]  = key, arr_num[j:]
                break         
    return arr_num


# selection sort 
def selection_sort(arr_num):
    for i in range(len(arr_num)):
        min_value_index_j = i
        for j in range(i+1,len(arr_num)):
            if arr_num[j] < arr_num[min_value_index_j]:
                min_value_index_j = j
        #print(i,arr_num ,arr_num[min_value_index_j])
        arr_num[i], arr_num[min_value_index_j] = arr_num[min_value_index_j], arr_num[i]
    return arr_num

        

# Driver code
arr_num = [9,8,7,6,5,4,3,2,1]
arr_num1 = [9,8,7,6,1,2,3,4,5]
#print("final Bubble sort:",bubble_sort(arr_num1))
#print("final insertion sort:",insertion_sort(arr_num1))
#print("final selection sort:",selection_sort(arr_num1))
