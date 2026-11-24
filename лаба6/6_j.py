n, m = map(int, input().split())

edges = []

for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

order = list(map(int, input().split()))

pos = [0] * (n + 1)

for i in range(n):
    pos[order[i]] = i

ok = True

for u, v in edges:
    if pos[u] >= pos[v]:
        ok = False
        break

if ok:
    print("YES")
else:
    print("NO")