from sys import stdin
i = int(input())

human = [list(map(int,stdin.readline().split())for _ in range(i))]

print(human)
