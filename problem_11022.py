from sys import stdin

a = int(input())

for _ in range(1,a+1):
    F,S = map(int,stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(_,F,S,F+S))
