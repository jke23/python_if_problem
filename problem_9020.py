def find_sosu():
    sosu = []
    for x in range(2,5001):
        error = 0
        for a in range(2,int(x**0.5)+1):
            if x%a == 0 :
                error += 1
                break
        if error == 0 :
            sosu.append(x)
    return sosu


sosu = find_sosu()

a= int(input())
for _ in range(a) :
    num = int(input())
    dist = 10000
    for i in range(0,len(sosu)) :
        if num < sosu[i]/2 :
            break
        else :
            if num-sosu[i] in sosu :
                if dist > abs(num-sosu[i]*2) :
                    index = i
                    dist = abs(num - sosu[i] * 2)

    print("{} {}".format(sosu[index],num-sosu[index]))
