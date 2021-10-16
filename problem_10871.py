from sys import stdin

a, b = map(int,input().split())
arr=list(map(int,stdin.readline().split()))
small_num=[]

for i in range(a):
    if i<b :
        small_num.append(i)
    else :
        continue

print()