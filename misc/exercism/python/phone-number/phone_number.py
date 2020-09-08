"""
See problem statement in README.md.
---
Understand - This problem is going to give as input
phone numbers with invalid format (including too many
numbers, bad characters, etc) and expect us to
either make a valid phone number consisting of
10 digits and nothing else, or raise an exception.
-----
Plan - part of this problem is simply going to be trial
and error as we account for the full range of ways people
can wrongly enter a number - we can catch some obvious cases by
stripping characters out (like -, ., and parens), but there
will be some red-to-green with the test cases as we
catch everything.

The general strategy is "remove expected bad characters,
then count the remaining characters and raise an exception
if we still do not have a valid phone number."

-----
Execute: see below.
-----
Review: This problem took a bit more effort than anticipated - I didn't fully cover
all of the rules for valid phone numbers (e.g. I missed while reading that the first
number of the area or exchange code couldn't be 0 or 1), so I wound up not catching cases
that should've been invalid. Initially, I also had to catch some extra cases even when all
tests passed (e.g., the test for "123-abc-7890" would pass because ValueError would be
raised, but because self.number was too short given that the 'abc' hadn't been added -
I had to specifically test for wrong characters and make sure to fail specifically because
they had been encountered).

This algorithm is O(c) for space (we only need to store a class and 10 digits), and O(N)
for a phone number input string of length(N) - technically, the phone number should be automatically
invalid if over a certain length, but it may contain more than 11 characters given parens, periods,
spaces, etc.
"""


class Phone(object):
    def __init__(self, phone_number):
        self.number = ''
        self.area_code = ''
        self.exchange_code = ''
        self.subscriber_number = ''

        for char in phone_number:
            if char.isdigit():
                self.number += char
            elif char not in ['-', '.', '(', ')', " ", "+"]:
                raise ValueError("Number contains invalid characters.")

        # Fail if the number length is wrong
        if 10 > len(self.number) or len(self.number) > 11:
            raise ValueError("Number is of incorrect length.")

        # Strip country code, or fail on invalid code
        if len(self.number) == 11:
            if self.number[0] == '1':
                self.number = self.number[1:]
            else:
                raise ValueError("Invalid country code.")

        # Splice into specific fields
        self.area_code = self.number[0:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]

        # Raise ValueError on invalid area or exchange codes
        if (int(self.area_code[0]) < 2):
            raise ValueError("Invalid area code.")

        if (int(self.exchange_code[0]) < 2):
            raise ValueError("Invalid exchange code.")

    def pretty(self):
        return "({0}) {1}-{2}".format(self.area_code, self.exchange_code, self.subscriber_number)
