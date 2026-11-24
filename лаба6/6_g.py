n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True

    for u in graph[v]:
        if not visited[u]:
            dfs(u)

if m != n - 1:
    print("NO")
else:
    dfs(1)

    if all(visited[1:]):
        print("YES")
    else:
        print("NO")