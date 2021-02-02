from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * (n+1)
        for first, last, count in bookings:
            flights[first-1] += count
            flights[last] -= count
        for i in range(1, n):
            flights[i] += flights[i-1]
        return flights[:-1]


s = Solution()
cases = [
    ([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5, [10, 55, 45, 25, 25])
]
for bookings, n, expected in cases:
    actual = s.corpFlightBookings(bookings, n)
    assert actual == expected, f"{bookings, n}: {expected} != {actual}"
