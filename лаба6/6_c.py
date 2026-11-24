n, m = map(int, input().split())

edges = set()

for i in range(m):
    a, b = map(int, input().split())
    edges.add((a, b))

ok = True

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if (i, j) not in edges:
            ok = False

if ok:
    print("YES")
else:
    print("NO")