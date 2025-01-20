from string import digits, ascii_lowercase


class Solution:
    def extract_digits(self, abbr, j):
        digits_arr = []
        while j < len(abbr) and abbr[j] in digits:
            digits_arr.append(abbr[j])
            j += 1
        return ''.join(digits_arr)

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j] in ascii_lowercase:
                if word[i] != abbr[j]:
                    print(f"Letter mismatch: {word[i]} != {abbr[j]}")
                    return False
                i, j = i+1, j+1
            else:  # word[i] in digits:
                digit_string = self.extract_digits(abbr, j)
                if digit_string[0] == '0':
                    print(f"Leading zero: {j} = {abbr[j]}")
                    return False
                i += int(digit_string)
                j += len(digit_string)

        return i == len(word) and j == len(abbr)


s = Solution()
for string, abbrev, expected in [
    ("a", "a", True),
    ("a", "1", True),
    ("substitution", "s10n", True),
    ("substitution", "sub4u4", True),
    ("substitution", "12", True),
    ("substitution", "su3i1u2on", True),
    ("substitution", "substitution", True),
    ("substitution", "s55n", False),
    ("substitution", "s010n", False),
    ("substitution", "s0ubstitution", False),
    ("internationalization", "i12iz4n", True),
    ("apple", "a2e", False)
]:
    actual = s.validWordAbbreviation(string, abbrev)
    assert actual == expected, f"{string}, {abbrev}: {actual} != {expected}"
