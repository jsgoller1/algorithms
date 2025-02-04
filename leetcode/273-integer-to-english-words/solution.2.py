"""
This problem is linear time (actually O(c) for space and time since limited on billions), but the difficulty will be around naming correctly.

345 - > three hundred forty five 
345000 -> three hundred forty five thousand 
345000000 -> three hundred forty five million 
etc

So we can go recursively in threes of digits / by orders of magnitude; 
thousands, millions, and billions

For groups of 3:
    n00: "n hundred"
    0n0: "teen, twenty, thirty, forty" (special handling for teens)
    00n: "one, two, three, etc"
"""

from collections import deque


MAGNITUDE = ["", "Thousand", "Million", "Billion"]
ONES = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
}
TEENS = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
}
TENS = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
}


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def recurse(value, magnitude) -> List[str]:
            if value == 0:
                return []
            words = []
            digits = value % 1000
            if digits >= 100:
                words.append(ONES[digits // 100])
                words.append("Hundred")
                digits = digits % 100

            if 20 <= digits:
                words.append(TENS[digits // 10])
                digits = digits % 10

            if 10 <= digits <= 19:
                words.append(TEENS[digits])
                digits = 0

            if 0 < digits:
                words.append(ONES[digits])

            if MAGNITUDE[magnitude] and words:
                words.append(MAGNITUDE[magnitude])
            return recurse(value // 1000, magnitude + 1) + words

        return " ".join(recurse(num, 0))
