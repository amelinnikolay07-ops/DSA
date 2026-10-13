n = int(input())
wagons = list(map(int, input().split()))

stack = []
need = 1

for wagon in wagons:
    stack.append(wagon)

    while stack and stack[-1] == need:
        stack.pop()
        need += 1

if not stack:
    print('YES')
else:
    print('NO')
