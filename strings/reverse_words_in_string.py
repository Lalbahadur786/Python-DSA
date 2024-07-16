# s1 = "welcome to dsa"  
# o/p = dsa to welcome

# idea
# first reverse the word in place by finding spaces
# then reverse the reversed string



def reverse(s, b, e):
    # reverse individual words
    while b < e:
        s[b], s[e] = s[e], s[b]
        b = b + 1
        e = e - 1

def reverse_words(s):
    b = 0
    for e in range(len(s)):
        if s[e] == " ":
            reverse(s, b, e-1)
            b = e + 1
    reverse(s, b, len(s)-1) # reverse last word
    reverse(s, 0, len(s)-1) # reverse reversed string
    return "".join(s)

s = "welcome to dsa"
print(s)
print(reverse_words(list(s)))

