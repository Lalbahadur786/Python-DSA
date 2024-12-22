# steps to perform descending order heap sort:
# 1. build heap with min-heapify
# 2. swap the min root to end
# 3. perform min-heapify from root
# 4. repeat step 2 and 3


def min_heapify(arr, N, i):
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i
    if l < N and arr[l] < arr[smallest]:
        smallest = l
    if r < N and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        # swap elems
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, N, smallest)

def build_heap(arr, N):
    startidx = N // 2 - 1 # bottom left parent idx
    for i in range(startidx, -1, -1):
        min_heapify(arr, N, i)
    return arr

def desc_heapsort(arr, N):
    arr = build_heap(arr, N)
    for i in range(N-1, 0, -1):
        # swap the min root to end
        arr[i], arr[0] = arr[0], arr[i]
        min_heapify(arr, i, 0)
    print(arr)

# arr = [100, 90, 80, 70, 50, 41, 25, 185]
arr = [4, 1, 3, 9, 7]
N = len(arr)
desc_heapsort(arr, N)
# heap sort
# In reality heap sort used with other alogs not indepentely