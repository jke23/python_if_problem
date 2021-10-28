a = int(input())

for x in range(a):
    h, w, v = map(int,input().split())
    width = v//h
    hight = v%h
    if hight == 0 :
        print(100*h+width)
    else :
        print(100*hight+(width+1))
