import collections


def getOddCounts(cntr):
    oddsCount = 0
    odds = []
    for letter, letterct in cntr.items():
        if letterct % 2:
            oddsCount += 1
            odds.append(letter)
    return oddsCount, odds


def handleEven(cntr, oddCounts):
    if oddCounts:
        return "NO SOLUTION"
    result = collections.deque()
    for letter, letterct in cntr.items():
        while letterct > 0:
            result.appendleft(letter)
            result.append(letter)
            letterct -= 2
    return "".join(result)


def handleOdd(cntr, oddCounts, odds):
    if oddCounts != 1:
        return "NO SOLUTION"
    result = collections.deque([odds[0] * cntr[odds[0]]])
    del cntr[odds[0]]
    for letter, letterct in cntr.items():
        while letterct > 0:
            result.appendleft(letter)
            result.append(letter)
            letterct -= 2
    return "".join(result)


def solve(string):
    cntr = collections.Counter(string)
    oddCounts, odds = getOddCounts(cntr)
    if len(string) % 2 == 0:
        return handleEven(cntr, oddCounts)
    else:
        return handleOdd(cntr, oddCounts, odds)


if __name__ == '__main__':
    print(solve(input()))
