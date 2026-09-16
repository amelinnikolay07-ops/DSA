def min_sum(n1, n2):
    n1.sort()
    n2.sort(reverse=True)
    return sum([n1[i] * n2[i] for i in range(len(n1))])


n1 = input().split()
n2 = input().split()
for i in range(len(n1)):
    n1[i] = int(n1[i])
    n2[i] = int(n2[i])

print(min_sum(n1, n2))
