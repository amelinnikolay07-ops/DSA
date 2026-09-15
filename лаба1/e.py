import sys

def MergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        left = MergeSort(left)
        right = MergeSort(right)

        return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

n = int(input())
if n > 10**5:
    sys.exit()

arr = list(map(int, input().split()))

for el in arr:
    if el > 10**9 or el < -10**9:
        sys.exit()

arr = MergeSort(arr)

print(*arr, sep=' ')
