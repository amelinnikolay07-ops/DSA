n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
tree = []

def dfs(v):
    visited[v] = True

    for u in graph[v]:
        if not visited[u]:
            tree.append((v, u))
            dfs(u)

dfs(1)

for a, b in tree:
    print(a, b)