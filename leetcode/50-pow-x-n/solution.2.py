class Solution:
    def myPow(self, x: float, n: int) -> float:
        n_cache = {0: 1.0, 1: x}

        def recurse(n):
            if n not in n_cache:
                n_cache[n] = recurse(n//2) * recurse(n//2) * (x if n % 2 else 1.0)
            return n_cache[n]
        return recurse(n) if n > 0 else (1 / recurse(-n))
