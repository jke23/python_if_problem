a = int(input())

i = 0
num = 0
while True :
    i += 1
    num += i
    if num >= a :
        num -= i
        break

n = a-num-1
if i%2 == 0 :
    print("{}/{}".format(n+1,i-n))
else :
    print("{}/{}".format(i-n,n+1))

