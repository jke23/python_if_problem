a = input()
count = len(a)
for i in range(len(a)):
    if a[i] == "=" :
        if a[i-1] == "c" or a[i-1] == "s":
            count -= 1
        elif a[i-1] == "z" :
            if a[i-2] == "d" :
                count -= 2
            else :
                count -= 1
    elif a[i] == "-" :
        count -= 1
    elif a[i] == "j" :
        if a[i-1] == "l" or a[i-1] == "n" :
            count -= 1

print(count)