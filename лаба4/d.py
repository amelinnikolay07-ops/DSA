import heapq
import sys

heap = []

for line in sys.stdin:
    command = line.split()

    if command[0] == "CLEAR":
        heap.clear()

    elif command[0] == "ADD":
        heapq.heappush(heap, -int(command[1]))

    elif command[0] == "EXTRACT":
        if heap:
            print(-heapq.heappop(heap))
        else:
            print("CANNOT")
