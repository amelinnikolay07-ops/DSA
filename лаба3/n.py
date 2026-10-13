from collections import deque

first = deque(map(int, input().split()))
second = deque(map(int, input().split()))

count = 0

while first and second and count < 10**6:
    a = first.popleft()
    b = second.popleft()

    if a == 0 and b == 9:
        first.append(a)
        first.append(b)
    elif a == 9 and b == 0:
        second.append(a)
        second.append(b)
    elif a > b:
        first.append(a)
        first.append(b)
    else:
        second.append(a)
        second.append(b)

    count += 1

if not first:
    print('second', count)
elif not second:
    print('first', count)
else:
    print('botva')
