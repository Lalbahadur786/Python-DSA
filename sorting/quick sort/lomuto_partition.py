a = [41, 54, 78, 65, 2 , 3, 50,  5, 50]
l = 0
h = 8
pivot = a[h]
i = l - 1
for j in range(l, h):
    if a[j] <= pivot:
        i += 1
        a[i], a[j] = a[j], a[i]
a[i+1], a[h] = a[h], a[i+1]
print(*a)