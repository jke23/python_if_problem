def calculate(array) :
    med_num = 0
    cal = ""
    second_num = 0
    med_num = array[0]
    for i in range(1,len(array),2) :
        cal = array[i+1]
        second_num = array[i+2]
        if cal == "+" :
            med_num += second_num
        elif cal == "-" :
            med_num -= second_num
        elif cal == "*":
            med_num *= second_num
        elif cal == "/":
            if med_num > 0 :
                med_num = med_num//second_num
            else :
                med_num = -1*(-1*med_num//second_num)

from sys import stdin
cal_x = []
a = int(stdin.readline())
num = list(map(int,stdin.readline().split()))
cal = list(map(int,stdin.readline().split()))
for x in range(4):
    if x == 0 :
        for _ in range(cal[x]) :
            cal_x.append("+")
    elif x == 1 :
        for _ in range(cal[x]) :
            cal_x.append("-")
    elif x == 2 :
        for _ in range(cal[x]) :
            cal_x.append("*")
    elif x == 3 :
        for _ in range(cal[x]) :
            cal_x.append("/")
