while True :
    a = int(input())
    if a > 0 :
        count = 0
        for x in range(a+1, a*2 + 1):
            error = 0
            if x > 1:
                for i in range(2, int(x ** 0.5) + 1):
                    if x % i == 0:
                        error += 1
                        break
                if error == 0:
                    count += 1
        print(count)
    else :
        break