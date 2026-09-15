import sys
import random

def quickSort(arr, left, right):
    if left < right:
        pivot = separation(arr, left, right)

        quickSort(arr, left, pivot-1)
        quickSort(arr, pivot+1, right)

    return arr

def separation(arr, left, right):
    pivot_index = random.randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    pivot = arr[right]

    real_left = left

    for current in range (left, right):
        if arr[current] < pivot:
            arr[real_left], arr[current] = arr[current], arr[real_left]
            real_left += 1

    arr[real_left], arr[right] = arr[right], arr[real_left]
    return real_left

n = int(input())
if n > 10**5:
    sys.exit()

arr = list(map(int, input().split()))

for elem in arr:
    if elem > 10**9 or elem < -10**9:
        sys.exit()

left = 0
right = n-1

arr = quickSort(arr, left, right)

print(*arr,sep=' ')
