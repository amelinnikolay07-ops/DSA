def good(arr, k, length):
    count = 0

    for wire in arr:
        count += wire // length

    return count >= k


n, k = map(int, input().split())

a = []

for _ in range(n):
    a.append(int(input()))

l = 0
r = max(a) + 1

while r - l > 1:
    m = (l + r) // 2

    if good(a, k, m):
        l = m
    else:
        r = m

print(l)
