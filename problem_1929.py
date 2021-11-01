
a,b = map(int,input().split())


sosu = []
for x in range(a,b+1) :
    error = 0
    if x > 1 :
        for i in range(2,int(x**0.5)+1) :
            if x%i == 0 :
                error += 1
                break
        if error == 0 :
            sosu.append(x)

print("\n".join(map(str,sosu)))