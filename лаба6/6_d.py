n, s = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

visited = [False] * n

def dfs(v):
    visited[v] = True
    count = 1

    for u in range(n):
        if matrix[v][u] == 1 and not visited[u]:
            count += dfs(u)

    return count

print(dfs(s - 1))