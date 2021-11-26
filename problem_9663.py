from sys import stdin

a = int(stdin.readline())

chess = [0]*a
visited = [False]*a
count = 0
hang = 0
for i in range(a) :
    chess[0] = i
    visited[i] = True
    for x in range(x) :
        visited[i + x] = True
        visited[i - x] = True