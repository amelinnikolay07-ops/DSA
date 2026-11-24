n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
components = []

for v in range(1, n + 1):
    if not visited[v]:
        stack = [v]
        visited[v] = True
        component = []

        while stack:
            current = stack.pop()
            component.append(current)

            for u in graph[current]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)

        components.append(component)

print(len(components))

for component in components:
    print(len(component))
    print(*component)