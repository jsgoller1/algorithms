def calculate_trailing_zeroes(n):
    total = 0
    power = 1
    while (5**power <= n):
        total += (n // 5**power)
        power += 1
    return total


if __name__ == '__main__':
    n = int(input())
    print(calculate_trailing_zeroes(n))
