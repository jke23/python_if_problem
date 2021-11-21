N, M = map(int, input().split())
out=[]

def solve (depth,M,N,i) :
    if depth == M :
        print(' '.join(map(str, out)))
        return
    for n in range(1,N+1):
        out.append(n)
        solve(depth+1,M,N,n)
        out.pop()

for i in range(1,N+1) :
    out.append(i)
    solve(1,M,N,i)
    out=[]

