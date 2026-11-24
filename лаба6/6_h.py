from collections import deque

n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

start, finish = map(int, input().split())

start -= 1
finish -= 1

dist = [-1] * n
parent = [-1] * n

q = deque([start])
dist[start] = 0

while q:
    v = q.popleft()

    for u in range(n):
        if matrix[v][u] == 1 and dist[u] == -1:
            dist[u] = dist[v] + 1
            parent[u] = v
            q.append(u)

if dist[finish] == -1:
    print(-1)
else:
    print(dist[finish])

    if dist[finish] > 0:
        path = []
        v = finish

        while v != -1:
            path.append(v + 1)
            v = parent[v]

        path.reverse()
        print(*path)