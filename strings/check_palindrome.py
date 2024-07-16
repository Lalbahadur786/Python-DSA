s1 = "abccba"

low = 0
high = len(s1) - 1
while low < high:
    if s1[low] != s1[high]:
        print("not a palindrome")
        break
    low = low + 1
    high = high - 1
else: # if while loop executed completely without break
    print("palindrome")