a = int(input())

base_1 = [21,x for x in range(a,0,-1)]
base_2 = [21]
base_3 = [21]
count = 0

base = base_1
while True :
    if base_1[-1] < base_3[-1] :
        base_3.append(base_1.pop())
        print("3 1")
        count += 1

