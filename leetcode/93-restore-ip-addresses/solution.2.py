from typing import List


def ip_invalid(ip_list):
    if not ip_list:
        return False
    return (len(ip_list) > 4) or \
        not (0 <= int(ip_list[-1]) <= 255) or \
        (ip_list[-1][0] == '0' and len(ip_list[-1]) > 1)


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid_addrs = []

        def find_valid(i, curr):
            if ip_invalid(curr):
                return
            if i >= len(s):
                valid_addrs.append('.'.join(curr)) if len(curr) == 4 else None
                return
            find_valid(i+1, curr + [s[i]])
            find_valid(i+1, curr[:-1] + [curr[-1] + s[i]]) if curr else None

        find_valid(0, [])
        return valid_addrs


sol = Solution()
cases = [
    ("25525511135", ["255.255.11.135", "255.255.111.35"]),
    ("0000", ["0.0.0.0"]),
    ("1111", ["1.1.1.1"]),
    ("010010", ["0.10.0.10", "0.100.1.0"]),
    ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"])
]
for s, expected in cases:
    actual = sol.restoreIpAddresses(s)
    assert sorted(actual) == sorted(expected), f"{s}: {sorted(expected)} != {sorted(actual)}"
