from collections import Counter

a = input()
b = input()


if len(a) != len(b):
    print("NO")
else:

    if Counter(a) == Counter(b):
        print("YES")
    else:
        print("NO")
