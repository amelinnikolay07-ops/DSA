import heapq

n = int(input())
heap = list(map(int, input().split()))

heapq.heapify(heap)

cost = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    sum = a + b
    cost += sum * 0.05

    heapq.heappush(heap, sum)

print(f'{cost:.2f}')
