while True :
    t_list = list(map(int,input().split()))
    if t_list[0] == 0 :
        break
    else :
        t_list.sort()
        if t_list[0]**2+t_list[1]**2 == t_list[2]**2 :
            print("right")
        else :
            print("wrong")