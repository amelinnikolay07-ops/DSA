def search(arr, key):
    l = -1
    r = len(arr)

    while r - l > 1:
        mid = (l + r) // 2

        if arr[mid] < key:
            l = mid
        else:
            r = mid

    if r < len(arr) and arr[r] == key:
        return True
    return False


N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for key in B:
    if search(A, key):
        print('YES')
    else:
        print('NO')
