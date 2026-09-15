s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("NO")
else:
    counts = {}

    for char in s1:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for char in s2:
        if char in counts:
            counts[char] -= 1
        else:

            print("NO")
            exit()

    is_anagram = True
    for count in counts.values():
        if count != 0:
            is_anagram = False
            break

    if is_anagram:
        print("YES")
    else:
        print("NO")
