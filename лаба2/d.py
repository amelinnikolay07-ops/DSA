def f(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

a, b, c, d = map(int, input().split())

l = -10000.0
r = 10000.0

for _ in range(100):
    m = (l + r) / 2

    if f(m, a, b, c, d) == 0:
        l = r = m
        break

    if f(l, a, b, c, d) * f(m, a, b, c, d) <= 0:
        r = m
    else:
        l = m

print(f'{(l + r)/ 2:.10f}')
