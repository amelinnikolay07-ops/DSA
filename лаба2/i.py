def count_number(arr, key):
    l = -1
    r = len(arr)

    while r - l > 1:
        m = (l + r) // 2

        if arr[m] < key:
            l = m
        else:
            r = m

    left = r
  
    l = -1
    r = len(arr)

    while r - l > 1:
        m = (l + r) // 2

        if arr[m] <= key:
            l = m
        else:
            r = m

    right = r

    return right - left


n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

for key in b:
    print(count_number(a, key), end=' ')
