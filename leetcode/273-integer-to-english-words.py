"""
Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 231 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
-----------------------------
Input: int
Output: String
Maximum value: 2,147,483,647 (two billion)

- This problem has around a 1-to-3 like to dislike ratio; maybe weird edge cases piss people off?
- We are going to need to do a lot of typing here xD; we should create a dict mapping ints to words
- We can split up a number based on 3-digits:
  2 | 147 | 483 | 647
  then for each of these, we directly translate it and add "billion", "million", "thousand"
- Then, we can translate a 3 digit by splitting it up too:
        1    | 4  |   7
  one hundred forty seven
-----------------------------------
translate(number)
- Convert the number to a string
- Keep global result, empty string
- Slice last 3 chars off
- Do 3-translate, prepend to result
- Do next slice, 3-traslate, if nonempty prepend with "thousand"
- same thing, but with million
- then with billion

3-translate(number)
  - look up last digit (if there is one), prepend translation
  - look up second digit (if there is one), prepend tens-translation
  - look up third digit (if there is one), prepend ones translation + "hundred" and return
"""
import random


class Solution(object):
    def __init__(self):
        self.ones = {"0": "", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six",
                     "7": "Seven", "8": "Eight", "9": "Nine"}
        self.teens = {"10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen",
                      "15": "Fifteen", "16": "Sixteen", "17": "Seventeen", "18": "Eighteen",
                      "19": "Nineteen"}
        self.tens = {"0": "", "2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty",
                     "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety"}
        self.places = ["", "Thousand", "Million", "Billion"]

    def threeTranslate(self, digits):
        translated = []
        print("threeTranslate() | {0}".format(digits))

        if len(digits) == 1:
            translated = [self.ones[digits]]
        else:
            if digits[-2:] in self.teens:
                translated = [self.teens[digits[-2:]]]
            else:
                translated = [self.tens[digits[-2]], self.ones[digits[-1]]]
        if len(digits) == 3 and digits[0] != '0':
            translated = [self.ones[digits[0]], "Hundred"] + translated
        return [string for string in translated if string]

    def numberToWords(self, num):
        if num == 0:
            return 'Zero'
        print("Original: {0}".format(num))
        solution = []
        num = str(num)
        place = 0
        while num:
            field = num[-3:]
            num = num[:-3]
            solution = self.threeTranslate(
                field) + [self.places[place]] + solution
            place += 1
            print(solution)

        return ' '.join([string for string in solution if string])


s = Solution()
for i in range(100):
    print(s.numberToWords(random.randint(0, 2147483647)))

assert s.numberToWords(0) == 'Zero'
assert s.numberToWords(123) == "One Hundred Twenty Three"
assert s.numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
assert s.numberToWords(
    1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
assert s.numberToWords(
    1234567891) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
assert s.numberToWords(
    2037223010) == "Two Billion Thirty Seven Million Two Hundred Twenty Three Thousand Ten"
assert s.numberToWords(1000000) == "One Million"
