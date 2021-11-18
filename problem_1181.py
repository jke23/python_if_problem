import sys

n = int(sys.stdin.readline())
so = []
for i in range(n):
    word = str(sys.stdin.readline().rstrip())
    if word not in so :
        so.append(word)
so.sort(key=lambda x: (len(x), x))
for i in so:
    print(i)