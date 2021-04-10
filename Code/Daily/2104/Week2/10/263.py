class Solution:
    def isUgly(self, n: int) -> bool:
        while n > 0 and n % 2 == 0:
            n /= 2
        while n > 0 and n % 3 == 0:
            n /= 3
        while n > 0 and n % 5 == 0:
            n /= 5
        return n == 1