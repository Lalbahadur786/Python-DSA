s1 = "abccbd"
# here is b is the leftmost repeating character

CHAR = 256

visited = [False] * CHAR
res = None
for i in range(len(s1)-1, -1, -1):
    if visited[ord(s1[i])] == True:
        res = i
    else:
        visited[ord(s1[i])] = True

print(s1[res])
