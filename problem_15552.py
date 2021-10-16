from sys import stdin

a = int(input())

for _ in range(a):
    F,S = map(int,stdin.readline().split())
    print(F+S)
