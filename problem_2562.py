Standard_num=0
i=0
while True:
    try :
        a=int(input())
        i += 1
        if a > Standard_num :
            Standard_num = a
            count = i
    except :
        break

print(Standard_num)
print(count)