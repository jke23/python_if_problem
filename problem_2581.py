from functools import reduce

a = int(input())
b = int(input())

sosu = []
for x in range(a,b+1) :
    error = 0
    if x == 1 :
        continue
    else:
        for i in range(2,x) :
            if x%i == 0 :
                error += 1
            else :
                continue
    if error == 0 :
        sosu.append(x)
if len(sosu) > 0 :
    print(reduce(lambda x,y: x + y, sosu))
    print(sosu[0])
else :
    print(-1)