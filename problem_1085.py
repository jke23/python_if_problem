x, y, w, h = map(int,input().split())
dist = []
dist.append(x)
dist.append(y)
dist.append(w-x)
dist.append(h-y)
dist.sort()
print(dist[0])

