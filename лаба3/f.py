from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

d = deque()

for i in range(n):
    while d and d[0] <= i - k:
        d.popleft()

    while d and a[d[-1]] >= a[i]:
        d.pop()

    d.append(i)

    if i >= k - 1:
        print(a[d[0]])
