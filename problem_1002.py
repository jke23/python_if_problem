a = int(input())

for _ in range(a) :
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    dist = ((x1-x2)**2+(y1-y2)**2)**0.5
    sum_r = r1 + r2

    if x1 == x2 and y1 == y2 :
        if r1 == r2 :
            print("-1")
        else :
            print("0")

    else :
        if dist > sum_r :
            print("0")
        elif dist == sum_r :
            print("1")
        else :
            if r1 > dist + r2 or r2 > dist + r1 :
                print("0")
            elif r1 == dist + r2 or r2 == dist + r1 :
                print("1")
            else :
                print("2")