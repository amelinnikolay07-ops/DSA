from collections import deque

n = int(input())

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

moves = [
    (-2, -1), (-2, 1),
    (2, -1), (2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2)
]

dist = [[-1] * n for i in range(n)]
parent = [[None] * n for i in range(n)]

q = deque([(x1, y1)])
dist[x1][y1] = 0

while q:
    x, y = q.popleft()

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                parent[nx][ny] = (x, y)
                q.append((nx, ny))

path = []
x, y = x2, y2

while (x, y) != (x1, y1):
    path.append((x + 1, y + 1))
    x, y = parent[x][y]

path.append((x1 + 1, y1 + 1))
path.reverse()

print(dist[x2][y2])

for x, y in path:
    print(x, y)