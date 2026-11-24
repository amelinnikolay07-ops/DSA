n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

sources = []
sinks = []

for i in range(n):
    if all(matrix[j][i] == 0 for j in range(n)):
        sources.append(i + 1)

    if all(matrix[i][j] == 0 for j in range(n)):
        sinks.append(i + 1)

print(len(sources))
print(*sources)

print(len(sinks))
print(*sinks)