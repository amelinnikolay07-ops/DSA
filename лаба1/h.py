from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


n = int(input())
Points = []

for i in range(n):
    x, y = map(int, input().split())

    Points.append(Point(x, y))
Points.sort(key=lambda p: p.x**2 + p.y**2)
for p in Points:
    print(p.x, p.y)
