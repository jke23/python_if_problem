import sys

n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(str,sys.stdin.readline().split())))
    so[i].append(i)

so.sort(key=lambda x: (int(x[0]), x[2]))

for i in so:
    print(" ".join(i[0:2]))