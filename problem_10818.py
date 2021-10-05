import sys

a=int(input())
num=list(map(int,sys.stdin.readline().split()))
num.sort()
print("{} {}".format(num[0],num[a-1]))