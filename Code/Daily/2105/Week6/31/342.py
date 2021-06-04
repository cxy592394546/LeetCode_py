from math import sqrt


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        val = int(sqrt(n))
        if val ** 2 != n:
            return False
        return val == val & -val
