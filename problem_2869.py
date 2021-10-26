a, b, c =map(int,input().split())
if a == c :
    print("1")
else :
    x = c - a
    day = x%(a-b)
    if day == 0 :
        print(x//(a-b)+1)
    elif day != 0:
        print(x//(a-b)+2)