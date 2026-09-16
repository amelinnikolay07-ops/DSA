n = int(input())

a = list(range(1, n + 1))

for i in range(1, n):
    a[i], a[i // 2] = a[i // 2], a[i]

print(*a)
