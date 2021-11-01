a = int(input())

x = 2
if a>1 :
    while True:
        if a%x == 0 :
            if a//x == 1 :
                print(x)
                break
            else :
                a = a/x
                print(x)
        else :
            x += 1



