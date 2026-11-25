n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

color = [0] * (n + 1)

def dfs(v, c):
    color[v] = c

    for u in graph[v]:
        if color[u] == 0:
            if not dfs(u, 3 - c):
                return False
        elif color[u] == c:
            return False

    return True

ok = True

for v in range(1, n + 1):
    if color[v] == 0:
        if not dfs(v, 1):
            ok = False
            break

if ok:
    print("YES")
    for v in range(1, n + 1):
        if color[v] == 1:
            print(v, end=" ")
else:
    print("NO")
