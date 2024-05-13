
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr [i]:
        largest = l
    if r < n and arr[r] > arr [i]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr [largest], arr[i]


def heap_sort(arr, n):
    # Heapify the arr
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)



arr = [10, 1, 2, 3, 54, 34, 85]
heap_sort(arr, len(arr))
print(*arr)