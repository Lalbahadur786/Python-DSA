import heapq
li = [5, 7, 9, 1, 3]

heapq.heapify(li) # min heap
print("heapify list:", li)

heapq.heappush(li, 4)
print("modified heap after push 4:", li)

heapq.heappop(li) # pop smallest elem i.e. root
print("heap after popping root", li)
heapq.heappushpop(li, 10)
print("heap after heappushpop", li)
heapq.heapreplace(li, 17)
print("n largest", heapq.nlargest(2, li))
print("n smallest", heapq.nsmallest(2, li))