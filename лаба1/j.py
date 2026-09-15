from sys import stdin

arr = []
for line in stdin:
    arr.append(line.rstrip())

n = len(arr)
for iter in range(n - 1):
    swapped = False
    for i in range(n - iter - 1):
        if arr[i] + arr[i + 1] < arr[i + 1] + arr[i]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
    if not swapped:
        break
print(''.join(arr))
