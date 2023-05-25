def true_solution(coins):
    coins = sorted(coins)
    contig_sum = 0
    bad_idx = -1

    # First, find where in the array the contiguous
    # set of numbers ends. If it's the entire array,
    # solution is trivial (sum + 1)
    for i, coin in enumerate(coins):
        if coin != i+1:
            bad_idx = i
            break
        contig_sum += coin
    if bad_idx == -1:
        return contig_sum + 1

    # Else, continue looking until we find a coin value greater
    # than our current max sum. Any coins we find less than this
    # just increase our max sum and give ways to create new sums between
    # old max sum and new max sum. Any coins we find greater than our current
    # max sum leave a gap, in which the first value is the lowest value we cannot create.
    while bad_idx < len(coins):
        coin = coins[bad_idx]
        if coin > contig_sum+1:
            break
        contig_sum += coin
        bad_idx += 1
    return contig_sum + 1


if __name__ == '__main__':
    n = int(input())
    coins = [int(val) for val in input().split(" ")]
    # print(coins)
    print(true_solution(coins))
