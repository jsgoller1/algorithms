class Solution:
    """
    Key ideas here:
    recursion breaks down the number:
        x^n = x^(n/2) * x^(n^2), i.e. we add exponents when we multiply their bases together
    But iteration builds it up:
        x * x * x * x = x^4
        x^4 * x^4 = x^8
        x^8 * x^8 = x^16
    So think about the exponent. If x^10, 10 = 1010. So 10 = 2^1 + 2^3
    So x^10 = x^(2^1 + 2^3) = x^2^1 * x^2^3. 
    Start the total off as x^0 = 1. 
    Does our exponent include (2^1)? If so, multiply our total times the base
    Then shift the exponent left, and square the base. 
    Does it include 2^2 (now determined by 1s place)? If not, skip it. 
    Do this until the exponent is 0. 
    """

    def myPow(self, x, n):
        neg, n = n < 0, abs(n)
        base = x
        total = 1
        while n:
            if n % 2:
                total *= base
            base *= base
            n = n // 2
        return 1 / total if neg else total


class SolutionRecursive:
    def myPow(self, x: float, n: int) -> float:
        cache = {0: 1.0, 1: x}

        def _pow(n):
            if n not in cache:
                cache[n] = (_pow(n-1) * x) if (n %
                                               2) else (_pow(n // 2) * _pow(n // 2))
            return cache[n]

        return _pow(n) if n < 0 else 1 / _pow(abs(n))
