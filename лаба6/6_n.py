n = int(input())

graph = [[] for i in range(n + 1)]

for i in range(1, n + 1):
    a = int(input())
    graph[i].append(a)

color = [0] * (n + 1)
count = 0

def dfs(v):
    global count

    color[v] = 1

    for u in graph[v]:
        if color[u] == 0:
            dfs(u)

        elif color[u] == 1:
            count += 1

    color[v] = 2

for v in range(1, n + 1):
    if color[v] == 0:
        dfs(v)

print(count)