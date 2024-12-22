# heap sort
# perform build heap with max-heapify
#it starts from parent node at left side

def max_heapify(arr, N, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < N and arr[l] > arr[largest]:
        largest = l
    if r < N and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        # swap elems
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, N, largest)



def build_heap(arr, N):
    startidx = N // 2 - 1 # bottom left parent idx
    for i in range(startidx, -1, -1):
        max_heapify(arr, N, i)
    return arr

def heapsort(arr, N):
    arr = build_heap(arr, N)
    for i in range(N-1, 0, -1):
        # swap the max root to end
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)
    print(arr)

# arr = [100, 90, 80, 70, 50, 41, 25, 185]
arr = [4, 1, 3, 9, 7]
N = len(arr)
heapsort(arr, N)
# heap sort
# In reality heap sort used with other alogs not indepentely 