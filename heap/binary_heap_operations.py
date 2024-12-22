import math
class MyMinHeap:
    def __init__(self):
        self.arr = []
        
    def __init__(self, lst):
        if not lst:
            raise Exception("No empty list allowed.")
        self.arr = lst
        # get the last parent node from right of binary tree
        i = (len(lst) - 2) // 2
        while i >= 0:
            self.min_heapify(i)
            i = i - 1

    def get_parent(self, i):
        return  (i-1) // 2
    def get_left_child(self, i):
        return (2*i+1)
    def get_right_child(self, i):
        return (2*i+2)
    def insert(self, key):
        self.arr.append(key)
        i = len(self.arr) - 1
        while i > 0 and self.arr[self.get_parent(i)] > self.arr[i]:
            p = self.get_parent(i)
            self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
            i = p


    def min_heapify(self, i):
        # start from root and go till where this greater 
        # root element can be fixed
        smallest = i
        # step 1 get the children
        lt = self.get_left_child(i)
        rt = self.get_right_child(i)
        n = len(self.arr)
        # Now compare root with left and right child and find min child
        if lt < n and self.arr[lt] < self.arr[smallest]:
            smallest = lt
        if rt < n and self.arr[rt] < self.arr[smallest]:
            smallest = rt
        # if found other node less than current root
        # Then swap
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)
    
    def extract_min(self):
        # this means removing the min elem root from the heap and 
        # perform minheapify to keep heap properties intact

        # step 1: assign last node to root
        self.arr[0] = self.arr[-1]
        # step 2: pop last element
        self.arr.pop()
        # till now min element is removed
        # but greater number at root need to minheapify that
        self.min_heapify(0)
        
    def decrease_key(self, i, x):
        # this will replace value at i with x
        # then need to heapfy the binary heap min_heapfiy
        self.arr[i] = x
        while i != 0 and self.arr[self.get_parent(i)] > self.arr[i]:
            p = self.get_parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p


    def delete(self, i):
        if i < len(self.arr):
            self.decrease_key(i, -math.inf) # replace delete idx with -inf
            self.extract_min()


# myminh  = MyMinHeap()
# for i in [47, 1, 69, 2, 75, 84]:
#     myminh.insert(i)
# print(f"insert: {myminh.arr}")
# # myminh.extract_min()
# # print(f"extract_min: {myminh.arr}")
# myminh.decrease_key(4, 3)
# print(f"decrease_key: {myminh.arr}")
# myminh.delete(4)
# print(f"delete: {myminh.arr}")

# for build heap
myminh  = MyMinHeap([47, 1, 69, 2, 75, 84])
print(f"build heap: {myminh.arr}")