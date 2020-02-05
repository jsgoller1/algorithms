"""
Consider the problem of "finding a needle in a haystack".  In other words, given two strings `needle` and `haystack`, we want to determine whether `needle` occurs as a substring of `haystack`, and if so, where it occurs.

1. Implement a brute-force approach for solving this problem.

- What's the worst-case running time for your implementation?
    - Approximately O(n^2); if we check the full length of the remaining superstring for the substring at each character. This is shown below.
- What are some "pathological" inputs that would cause such worst-case performance?
    - As shown below, trying to do a substring check where we wind up evaluating most of the superstring
    each time will likely be bad. I think the hardest-to-detect and worst case of this is the final one shown below.
- How would your implementation perform on "typical" inputs?
    - Probably approximately O(n). I will test this.

2. What are some specific use-cases where this problem might come up (for example, using Ctrl-F to search through a webpage)?  
What are the relevant design constraints in these various cases?  In which cases would a brute-force approach be sufficient?
    - Brute force OK
        - Any situation where the user is OK waiting for a noticeable amount of time, or where we have lots of computing resources available.
        - Database queries, like a SQL MATCH statement might be OK if we have a sufficiently powerful machine and can do offline processing. 
    - Brute force insufficient
        - Design constraints: limited time before completion, limited computing resources, limited memory
        - Packet filtering, especially if we are looking for malicious input (like someone sending an exploit); I think filtering
          would require near nanosecond performance to ensure that network traffic isn't slowed noticeably.
        - grep - this is especially going to be necessary when looking through large logs (like syslog). 

"""


def str_eq(str1, str2):
    """
    Manually compare two strings; I specifically
    wrote this instead of using == to ensure my
    comparison was as brute-force-y as possible.
    """
    if len(str1) != len(str2):
        return False
    for i, _ in enumerate(str1):
        if str1[i] != str2[i]:
            return False
    return True


def substring(possible_substr, super_str):
    """
    Dumb substring test. Try every possible position
    in the superstring for the substring until we either
    reach a match or the end of the superstring.
    """

    # Assume the empty string is a substring of every string.
    if possible_substr == "":
        return 0

    for i, _ in enumerate(super_str):
        if str_eq(super_str[i : i + len(possible_substr)], possible_substr):
            return i
    return -1


if __name__ == "__main__":
    # Basic functionality
    assert substring("", "") == 0
    assert substring("a", "a") == 0
    assert substring("hua", "joshua") == 3
    assert substring("nope", "definitely won't be in this superstring") == -1

    # One bad case
    assert substring("cyberpunk", "cyberpun" * 1000) == -1

    # This case is relatively easy to get around with a simple check
    # that the superstring has enough characters remaining that it could
    # contain the substring, but will cause O(n^2) performance for a basic
    # brute force.
    assert substring("a" * 100, "a" * 99) == -1

    # Even so, with that length check, this one will still be bad
    assert substring("a" * 99, ("a" * 98) + ("b" * 10)) == -1
