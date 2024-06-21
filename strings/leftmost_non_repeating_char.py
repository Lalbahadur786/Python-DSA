# s1 = "abbcd"  c is leftmost non repeating character
import sys

s1 = "bbbcd"
CHAR = 256
fi = [-1] * CHAR

for i in range(len(s1)):
    if fi[ord(s1[i])] == -1:
        # not already occured
        fi[ord(s1[i])] = i
    else:
        # Already occured
        fi[ord(s1[i])] = -2
res = sys.maxsize
for i in range(CHAR):
    if fi[i] >= 0:
        res = min(res, fi[i])
if res == sys.maxsize:
    print(-1)
else:
    print(s1[res])
