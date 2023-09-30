from string import digits


class InvalidAbbr(Exception):
    pass


def parse_abbr(abbr):
    parsed = []
    curr = ""
    for char in abbr:
        if char in digits:
            if not curr and char == "0":
                raise InvalidAbbr
            curr += char
        else:
            if curr:
                parsed.append(int(curr))
                curr = ""
            parsed.append(char)
    if curr:
        parsed.append(int(curr))
    return parsed


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not (word and abbr):
            return word == abbr

        try:
            parsed_abbr = parse_abbr(abbr)
        except InvalidAbbr:
            return False

        i = 0
        for item in parsed_abbr:
            if i >= len(word):
                return False
            if isinstance(item, int):
                i += item
            elif word[i] == item:
                i += 1
            else:
                return False
        return i == len(word)


s = Solution()
cases = [
    ("internationalization", "i12iz4n", True),
    ("abcdef", "abc3", True),
    ("abcdef", "6", True),


    ("hi", "1hi", False),
    ("", "a", False),
    ("a", "", False),
    ("apple", "a2e", False),
    ("foobar", "f15", False),
    ("abcdef", "7", False),
    ("foobar", "foobar15", False),
    ("foobar", "fooba", False),
    ("foo", "03", False)

]
for i, case in enumerate(cases):
    word, abbv, expected = case
    actual = s.validWordAbbreviation(word, abbv)
    assert actual == expected, f"{i}: {word}, {abbv}: {actual} != {expected}"
