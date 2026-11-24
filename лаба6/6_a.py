n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

ok = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            ok = False

        if i == j and matrix[i][j] != 0:
            ok = False

if ok:
    print("YES")
else:
    print("NO")