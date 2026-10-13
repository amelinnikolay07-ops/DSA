from collections import deque
import sys

n = int(input())
deq1 = deque()  # левая часть
deq2 = deque()  # правая часть
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == '+':
        deq2.append(command[-1])
    elif command[0] == '*':
        deq2.appendleft(command[-1])
    else:
        print(deq1.popleft())

    if len(deq1) < len(deq2):
        deq1.append(deq2.popleft())
    elif len(deq1) > len(deq2) + 1:
        deq2.appendleft(deq1.pop())
