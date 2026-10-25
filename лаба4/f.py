import heapq

n = int(input())

a = []
for _ in range(n):
    t, l = map(int, input().split())
    a.append((t, l))

a.sort()

heap = []
answer = 0

for t, l in a:
    while heap and heap[0] <= t:
        heapq.heappop(heap)

    heapq.heappush(heap, t + l)

    answer = max(answer, len(heap))

print(answer)
