def is_palindrome(string, i):
    if (i > len(string)//2):
        return True
    ans = False
    if (string[i] is string[len(string) - i - 1] and is_palindrome(string, i+1)):
        ans = True
    return ans


string = "abbac"
print(is_palindrome(string, 0))
