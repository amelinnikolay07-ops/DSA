def search(arr, key):
    l = 0
    r = len(arr) - 1

    while r - l > 1:
        mid = (l + r) // 2

        if arr[mid] < key:
            l = mid
        else:
            r = mid

    if abs(arr[l] - key) <= abs(arr[r] - key):
        return arr[l]
    else:
        return arr[r]


N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for key in B:
    print(search(A, key))
