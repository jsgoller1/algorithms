from test_framework import generic_test


"""
Brute force: check every substring in t of len(s). O(n^2) time.

Naive approach; for each character in t, check if it's the first character in s. If so,
see if the next in t is a match on the next in s. Continue this until a match or failure.
If a failure occurs, don't go back to the start of t (we already checked all characters between
it and the failure); continue from failure. O(n) time, O(c) space. Does this work? No. 

This approach fails if starting the pattern match at s[i] ends at s[i+n] in failure
so we skip over all chars between s[i] and s[i+n], but would've found a match if we started
at s[i+m] where m < n. When might this occur? If all preceding n-1 characters matched,
but the nth did not, and we would somehow have to be able to "slide P forward in T" and
obtain a match. Example: P = aaacaaacd, T = aaacaaacaaacd.

Knuth-Morris-Pratt: Suppose we followed the naive approach, but instead of resetting p_idx
each time a failure occurs, we "backtrack" to the last location in T where 

"""


def compute_lps(pattern):
    lps = [0] * len(pattern)
    # i is the current char of the prefix,
    # j is the current char of the suffix
    i, j = 0, 1
    while j < len(pattern):
        if pattern[j] == pattern[i]:
            # a single char of the prefix and suffix (at the end of each)
            # matches. We can record it as our best for this position and
            # advance each index.
            i += 1
            lps[j] = i
            j += 1
        else:
            if i == 0:
                # If we mismatch and we haven't
                # matched a prefix and suffix yet, we can't move
                # i forward because we still have to match it to something.
                # j moves forward to try the next character.
                lps[j] = 0
                j += 1
            else:
                # if we mismatch and we have matched a prefix with the suffix,
                # we can't record the best suffix / prefix yet, because of the mismatch.
                # instead, we have to send the prefix back to where it was when we got the
                # best prefix/suffix match for the previous character. This may send us back to 0.
                i = lps[i - 1]

    return lps


def kmp(t: str, s: str) -> int:
    if s == "":
        return 0
    lps = compute_lps(s)
    t_idx = s_idx = 0
    while t_idx < len(t):
        if t[t_idx] == s[s_idx]:
            # Chars match; one step closer to full match
            t_idx += 1
            s_idx += 1
        else:
            if s_idx == 0:
                # The chars didn't match, but we haven't matched any
                # in the pattern yet anyways, so just go to the next
                # char of t and try again
                t_idx += 1
            else:
                # This is the crux of the algorithm. Only go back in
                # s to the point where we know we will still match,
                # because we precomputed matching prefixes and suffixes.
                s_idx = lps[s_idx - 1]
        if s_idx == len(s):
            # Full match; return the index it starts at.
            return t_idx - s_idx
    return -1


def rabin_karp(t: str, s: str) -> int:
    return kmp(t, s)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
