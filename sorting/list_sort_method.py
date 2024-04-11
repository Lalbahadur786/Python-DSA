# normal sort utility

lst = ["course", "geek", "random", "geek"]
# lst.sort()
# print(lst) # ['course', 'geek', 'geek', 'random']


# def sort_on_len(item):
#     return len(item)


# lst.sort(key=sort_on_len, reverse=False)
# print(lst) # ['geek', 'geek', 'course', 'random']

# using seperate method
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# def my_fun(p):
#     return p.x


# lst1 = [Point(1, 15), Point(5, 10), Point(1, 8)]
# lst1.sort(key=my_fun)

# for i in lst1:
#     print(i.x, i.y)

# using lt method ex 1
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __lt__(self, other):
#         return self.x < other.x


# lst2 = [Point(1, 15), Point(5, 10), Point(1, 8)]
# lst2.sort()
# for i in lst2:
#     print(i.x, i.y)

# using lt method ex 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x


lst3 = [Point(1, 15), Point(5, 10), Point(1, 8)]
lst3.sort()
for i in lst3:
    print(i.x, i.y)
