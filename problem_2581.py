
a = int(input())
b = int(input())

sosu = []
for x in range(a,b+1) :
    error = 0
    if x > 1 :
        for i in range(2,x) :
            if x%i == 0 :
                error += 1
                break
        if error == 0 :
            sosu.append(x)
        
if len(sosu) > 0 :
    print(sum(sosu))
    print(sosu[0])
else :
    print(-1)