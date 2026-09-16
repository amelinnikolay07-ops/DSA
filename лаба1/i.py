from collections import Counter

wrd1 = input()
wrd2 = input()


if len(wrd1) != len(wrd2):
    print("NO")
else:

    if Counter(wrd1) == Counter(wrd2):
        print("YES")
    else:
        print("NO")
