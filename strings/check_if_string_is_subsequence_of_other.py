s1 = "ABCDABCDABCE" #main string
s2 = "ABAB" # serach this subsequence in s1

# iterative way
# i, j = 0, 0

# while i < len(s1) and j < len(s2):
#     if s1[i] == s2[j]:
#         j += 1
#     i += 1

# if j == len(s2):
#     print(f"{s2} is subsequence")
# else:
#     print(f"{s2} is not a subsequence")

def is_sub_seq(s1, s2, m, n):
    """
    doing in reverse order right to left
    """
    if n == 0:
        return True
    if m == 0:
        return False
    if s2[n-1] == s1[m-1]:
        return is_sub_seq(s1, s2, m-1, n-1)
    else:
        return is_sub_seq(s1, s2, m-1, n)

print(is_sub_seq(s1, s2, len(s1), len(s2)))