lst = [10, -12, 8, -2]
lst_sorted = sorted(lst, key=abs)
# print(lst_sorted)  # [-2, 8, 10, -12]

tupl = (10, 14, 8, -2, 0)
tup_sorted = sorted(tupl)
print(tup_sorted)  # [-2, 0, 8, 10, 14]

sets = {14, 74, 87, 15, 2}
set_sorted = sorted(sets)
print(set_sorted)  # [2, 14, 15, 74, 87]

dict1 = {1: "hello", 5: "Good", 3: "morning"}
dict_sorted = sorted(dict1)
print(dict_sorted)  # [1, 3, 5]

list_tup = [(1, 5), (15, 5), (1, 4), (15, -1)]
list_tup_sorted = sorted(list_tup)
print(list_tup_sorted)  # [(1, 4), (1, 5), (15, -1), (15, 5)]
