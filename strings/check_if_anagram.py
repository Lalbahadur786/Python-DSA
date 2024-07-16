# Anagram
# if s1 and s2 len is same, having same numbers of chars but order can be different
# listen , silent are anagram

def are_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    # maintin count list
    count = [0] * 256  # extended ASCII chars

    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count [ord(s2[i])] -= 1
    
    for x in count:
        if x != 0:
            return False
    return True

s1 = "listen"
s2 = "silent"
print(are_anagram(s1, s2))