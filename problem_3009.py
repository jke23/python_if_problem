def find_dot(n) :
    a = n[0]
    for x in range(1,3):
        if a == n[x] :
            n.remove(a)
            n.remove(a)
            value = n[0]
            break
        else :
            value = a
    return value

list_x = []
list_y = []

for i in range(3):
    a, b = map(int,input().split())
    list_x.append(a)
    list_y.append(b)



print("{} {}".format(find_dot(list_x),find_dot(list_y)))