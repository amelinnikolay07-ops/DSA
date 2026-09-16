from random import *

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    val = arr[randint(0, len(arr) - 1)]
    left = [i for i in arr if i < val]
    center = [i for i in arr if i == val]
    right = [i for i in arr if i > val]
    return fast_sort(left) + center + fast_sort(right)


n = int(input())
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])

arr = quick_sort(arr)
print(*arr)
