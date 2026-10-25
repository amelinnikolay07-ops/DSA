import heapq

n = int(input())

heap = []

for i in range(n):
    x = int(input())
    t = max(1, 1000 - x)
    heapq.heappush(heap, (t, i, x))

current_time = 0
current_pos = 0

while heap:
    t, i, x = heapq.heappop(heap)

    if current_time + abs(current_pos - i) > t:
        print(t)
        break

    current_time = t
    current_pos = i

    x += 1
    next_time = t + max(1, 1000 - x)

    heapq.heappush(heap, (next_time, i, x))
