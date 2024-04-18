def union_of_lists(a, b):
    i = j = index = 0
    result = [0 for _ in range((len(a)+len(b)))]
    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            if index != 0 and a[i] == result[index - 1]:
                i += 1
            else:
                result[index] = a[i]
                i += 1
                index += 1
        else:
            if index != 0 and b[j] == result[index - 1]:
                j += 1
            else:
                result[index] = b[j]
                j += 1
                index += 1
    while i < len(a):
        if index != 0 and a[i] == result[index - 1]:
            i += 1
        else:
            result[index] = a[i]
            i += 1
            index += 1
    while j < len(b):
        if index != 0 and b[j] == result[index - 1]:
            j += 1
        else:
            result[index] = b[j]
            j += 1
            index += 1
    return [*result[:index]]

a = [2, 4, 4, 6, 8, 10]
b = [2, 3, 5, 8, 9]
b = [8, 9]
print(union_of_lists(a, b))