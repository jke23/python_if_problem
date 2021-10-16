while True :
    Med_list = list(map(int,input().split()))
    if bool(Med_list) is True :
        print(Med_list[0]+Med_list[1])
    else :
        break