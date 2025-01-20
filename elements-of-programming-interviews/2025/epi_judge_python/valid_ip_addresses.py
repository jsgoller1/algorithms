from typing import List

from test_framework import generic_test



def get_valid_ip_address(s: str) -> List[str]:
    if not (4 <= len(s) <= 12):
        return []
    ips = set()

    def valid_ip_segment(seg):
        return seg == '0' or \
              (1 <= int(seg) <= 255 and seg[0] != '0') 

    def recurse(segments, remaining):
        for i in range(1,4):
            new_seg = remaining[:i]
            new_remaining = remaining[i:]
            if valid_ip_segment(new_seg):
                segments.append(new_seg)
                if len(segments) == 4 and new_remaining == '':
                    ips.add('.'.join(segments))
                elif len(segments) < 4 and new_remaining:
                    recurse(segments, new_remaining)
                segments.pop()
    recurse([], s)
    return list(ips)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
