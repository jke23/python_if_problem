a = int(input())

for i in range(a) :
    k = int(input())
    n = int(input())
    people = [x for x in range(1,n+1)]

    for x in range(k) :
        for y in range(1,n) :
            people[y] += people[y-1]
    print(people[-1])