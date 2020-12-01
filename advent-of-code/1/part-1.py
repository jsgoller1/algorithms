"""
Problem:

After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars.
None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

In: List of numbers; two of them sum to 2020
Out: the product of the two numbers in the list that sum to 2020
-------------------
- List could be quite large; given input is 200 long
- Dumb: could just try all pairs; 200^2 is not huge
- Probably easier / less code:
    - numbers = set(input_list)
    - comps = set([2020 - val for val in numbers])
    - first = (numbers & comps)[0]
    - second = 2020 - first
    - answer = first * second
------
Actually don't even need to do second subtraction; each of the two elements will be in both lists and comps, so the intersection is enough

----------


"""

def main():
    numbers = set(int(val) for val in open('input.txt', 'r').read().split('\n') if val)
    comps = set([2020 - val for val in numbers])
    first, second = tuple((numbers & comps))
    print(first*second)

if __name__ == '__main__':
    main()    