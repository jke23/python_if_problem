
def fibonacci(n):
    dic={}
    if n in dic :
        return dic[n]

    global a, b
    if n == 0 :
        dic[0] = 0
        a+=1
        return 0
    elif n == 1 :
        dic[1] = 1
        b+=1
        return 1
    else :
        dic[n] = fibonacci(n-1) + fibonacci(n-2)
        return dic[n]


Test_num = int(input())
i=[]
while Test_num>=1 :
    i.append(int(input()))
    Test_num-=1

for t in i :
    a=0
    b=0
    fibonacci(t)
    print(a," ",b)