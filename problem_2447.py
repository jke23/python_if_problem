
def recursive_star(n, list) :
    if n == 3 :
        list = "**** ****"
        return list
    else :
        list = str(recursive_star(n / 3, list)*4 + " "*int(n/3)**2 + recursive_star(n / 3, list)*4)
        return list

a = int(input())
list_star = []
final = recursive_star(a,list_star)


for i in range(0,int(a/3)) :
    line_1 = ""
    line_2 = ""
    line_3 = ""
    if i == 0 :
        num = 0
    else :
        num = i*3*a
    for x in range(num,num+a*3-6,9):
        line_1 += final[x:x+3]
        line_2 += final[x+3:x+6]
        line_3 += final[x+6:x+9]
    print(line_1 + '\n' + line_2 + '\n' + line_3)
    print("---------------------------------------------------")
