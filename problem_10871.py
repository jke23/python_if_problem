from sys import stdin

a, b = map(int,input().split())
arr=list(map(int,stdin.readline().split()))
small_num=[]

for i in range(a):
    if arr[i]<b :
        small_num.append(arr[i])
    else :
        continue

print(" ".join(map(str,small_num)))