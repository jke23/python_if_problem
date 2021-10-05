import sys
a, b, c = map(int,sys.stdin.readline().split())

if c==b :
    print("-1")
elif c>b :
    print(int(a/(c-b))+1)
else :
    print("-1")