String = list(str(input().strip()))
alpabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = [-1 for i in range(len(alpabet))]

for i in range(0,len(String)):
    if String[i] in alpabet :
        n = alpabet.index(String[i])
        count[n] = i

print(" ".join(map(str,count)))