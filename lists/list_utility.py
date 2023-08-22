lst = [10, 14, 74, 50, 55]
print(-len(lst))
print(lst[-5])
# print(list(filter(lambda x: x > 10, lst)))

lst2 = [10]
lst3 = [11]
print("================")
for c in (lst, lst2, lst3):
    print(c)
print("This is second change")
