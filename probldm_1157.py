string = list(map(str,input().strip()))
string.lower()

for n in range(0,len(string)-1):
    for i in range(1,len(string)):
        if string[n] == string[i] :

