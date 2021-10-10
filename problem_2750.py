import sys
a = int(input())
b = list(int(input()) for _ in range(a))

b.sort()
for n in range(0,a) :
    print(b[n])
