import sys
a = int(input())
num = list(map(int,sys.stdin.readline().split()))
num.sort()
real_sosu=[]
sosu = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

if num[0] == 1 :
    del num[0]

for i in range(0,len(num)):
    error=0
    if num[i] in sosu:
        real_sosu.append(num[i])
    else:
        for n in range(0,len(sosu)):
            if num[i]%sosu[n] == 0 :
                error+=1
        if error == 0:
            real_sosu.append(num[i])

print(len(real_sosu))