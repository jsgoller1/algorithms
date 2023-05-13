def solve(n):
    if (n*(n+1)/2) % 2:
        print("NO")
        return None, None
    hi = n
    lo = 1
    set1 = []
    set2 = []
    if n % 2:
        set1.append(hi)
        hi -= 1

    while hi > lo:
        if (hi % 2):
            set1.append(hi)
            set1.append(lo)
        else:
            set2.append(hi)
            set2.append(lo)
        hi -= 1
        lo += 1

    return set1, set2


if __name__ == '__main__':
    n = int(input())
    set1, set2 = solve(n)
    if set1 and set2:
        # assert (sum(set1) == sum(set2))
        print("YES")
        print(len(set1))
        [print(val, end=" ") for val in set1]
        print(" ")
        print(len(set2))
        [print(val, end=" ") for val in set2]
