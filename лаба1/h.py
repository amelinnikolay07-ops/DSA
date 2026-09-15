from dataclasses import dataclass
import sys
from math import sqrt

@dataclass
class Point:
    x: int
    y: int

    def distance(self):
        return sqrt(self.x**2 + self.y**2)

n = int(input())
if n > 100:
    sys.exit()

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append(Point(x, y))

for i in range(n):
    minimum = arr[i].distance()
    for j in range(i+1, n):
        if arr[j].distance() < minimum:
            minimum = arr[j].distance()
            arr[i], arr[j] = arr[j], arr[i]


for i in range(n):
    print(arr[i].x, arr[i].y)
    
