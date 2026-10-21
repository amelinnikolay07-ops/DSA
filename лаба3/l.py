n, *a = map(int, input().split())

stack = []
ans = 0

a.append(0)

for i in range(n + 1):
    while stack and a[stack[-1]] > a[i]:
        h = a[stack.pop()]

        if stack:
            width = i - stack[-1] - 1
        else:
            width = i

        ans = max(ans, h * width)

    stack.append(i)

print(ans)
