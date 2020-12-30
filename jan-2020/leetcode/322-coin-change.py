"""
Input: list of coin denominations, target amount
Out: number of coins in solution using fewest coins

Possible cases:
    - 1 to 12 coins; no duplicates 
    - Value of coins between 1 and 2**31 - 1 (huge)
        - Can remove coins larger than the amount
    - Target amount between 0 and 10,000
    - Order of combination doesn't matter; [1,2,3] == 6 == [3,1,2]
------
    Slowest way - brute force:
        - find all combinations of coins equaling target amount
        -  10,000 - 12C1, !! - 12C1

    case 1: make 11 with [1,2,5]
        - [5, 5, 1]
        - [5, 2, 2, 1]
        - [5, 2, 1, 1 ,1]
        - [5, 1, 1, 1, 1, 1]
        - [2, 2, 1, 2, 2, 1, 1]
        - [2, 2, 1, 2, 1, 1, 1, 1]
        - [2, 2, 1, 1, 1, 1, 1, 1, 1]
        - [2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        - [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    Questions: 
        How can we detect that making change isn't possible:
        - [2,4] -> 11 # no divisors
        - [3] -> 10    # no divsors
        - [3,7,10] -> 15 # no divisors

        How can we detect it is possible:
        - [2,4] -> 10        # 2 divides 10 
        - [2,3,7,10] -> 15   # 3 divides 15
        - [2,3] -> 5         # 2+3 is 5, not a divisor 

    Maybe faster?
        - Start by making change with smallest denominations possible
        - Replace smaller coins with larger ones until none are replaceable
        
    Alternative
        - Start by getting as close as posssible to amount with largest coins
        - If largest coin leaves remainder, use smaller coins, and remove large
          coins one at a time til we can get correct denomination
          - E.g. get 117 using 25,10,5,3
                - Use 25 -> 100 - [25,25,25,25]
                - Can't use quarters anymore
                - Use 10 -> 110, [25,25,25,25,10]
                - Can't use dimes
                - Use 5 -> 115 [25,25,25,25,10,5]
                - Can't use 5
                - Can't use 3 
                - Remove 5 -> 110, [25,25,25,25,10]
                - Use 3 -> 113, 116, [25,25,25,25,10,3,3]
                - Can't use 3, 113 [25,25,25,25,10,3]
                - Can't use 3, 110 [25,25,25,25,10]
                - Can't use 10, 100 [25,25,25,25]
                - [25,25,25,25,10,5]
                (starting to feel recursive / tree search-y)
                - If a possible solution exists this way, we can find it by removing coins
                and trying smaller denominations; this will explode if we have a large value and small coins
                - When would we bail out?
                    - []
--------
    make_amount(coins, amount) -> coin count
    - Exit if:
        - amount in cache; return it. We start with 0 in the cache. 
        - we have no remaining coins; return -1
    - option 1: sub largest coin. if valid, make_amount with same coins and new amount. If it returns -1,
                we couldn't make change with that path, so don't bother caching. if it does work, cache it with +1.
    - if option 1 isn't valid:
        - option 2: remove largest coin. make_amount with same amount and new coins. if it works, cache and return the amount, don't add.
    otherwise -1. 
--------
Looked at solution; I'm close but not completely there.
    - make_amount(coins, amount):
        if amount == 0:
            return 0
        ways = []
        for coin in coins:
            if coin <= amount:
                ways.append(make_amount([coins], amount - coin))
        if not ways:
            return -1
        return min(ways)+1

"""
from typing import List



class Solution:
    def make_amount(self, coins, amount):
        """
        top_down(coins, amount):
            if amount is cached, return it
            
            ways = []
            for each coin:
                remainder: amount - coin
                if remainder in cache, append it + 1
                if remainder > 0, recurse on remainder
                if remainder = 0, append 1 to ways
                if remainder < 0, skip or append -1
                
            return lowest nonnegative value in ways, or -1 if not possible

        """
        if amount in self.cache:
           return self.cache[amount]      
        ways = []
        for coin in coins:
            remainder = amount - coin
            if remainder > 0:
                # If there's no way to make change for the remainder, don't append anything
                remainder_ways = self.make_amount(coins, remainder)
                ways += [remainder_ways+1] if remainder_ways != -1 else []
            if remainder == 0:
                ways.append(1)
            # Do nothing if remainder < 0, can't make change for it

        # Return the best way to make change, or -1 if we can't
        self.cache[amount] = min(ways) if ways else -1
        return self.cache[amount]

                

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.cache = {0:0}
        return self.make_amount(list(reversed(sorted(coins))), amount)


if __name__ == '__main__':
    s = Solution()
    test_cases = [
        (
            "Example 1",
            [1,2,5], 
            11,
            3
        ),
        (
            "No change",
            [2], 
            3,
            -1
        ),
        (
            "Base case",
            [1], 
            0,
            0
        ),
        (
            "Failed 1",
            [186,419,83,408],
            6249,
            20
        )
    ]
    for case in test_cases:
        name, coins, amount, expected = case
        actual = s.coinChange(coins, amount)
        assert actual == expected, f"Failed {name}: {amount},{coins} -- {actual} != {expected}"
        print("-----")