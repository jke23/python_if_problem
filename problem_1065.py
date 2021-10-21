han_num_list=[]
def han_num(number):
    if number < 100 :
        print(number)
    elif number >= 100 and number <= 1000 :
        for n in range(1,10) :
            for i in range(0,5) :
                if 2*i + n >= 10 :
                    continue
                else :
                    num_up = 100*n+10*(n+i)+(n+2*i)
                    if num_up <= number :
                        han_num_list.append(num_up)
        for x in range(9,0,-1) :
            for q in range(0,5) :
                if x - 2*q < 0 :
                    continue
                else :
                    num_down = 100*x+10*(x-q)+(x-2*q)
                    if num_down <= number:
                        if num_down not in han_num_list :
                            han_num_list.append(num_down)
        print(len(han_num_list)+99)

han_num(int(input()))