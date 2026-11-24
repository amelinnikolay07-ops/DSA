n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

color = [0] * n

def dfs(v):
    color[v] = 1

    for u in range(n):
        if matrix[v][u] == 1:
            if color[u] == 1:
                return True

            if color[u] == 0:
                if dfs(u):
                    return True

    color[v] = 2
    return False

cycle = False

for v in range(n):
    if color[v] == 0:
        if dfs(v):
            cycle = True
            break

if cycle:
    print(1)
else:
    print(0)