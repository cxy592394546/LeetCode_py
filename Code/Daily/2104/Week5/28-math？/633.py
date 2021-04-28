import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c)) + 1):
            if int(math.sqrt(c - i ** 2)) == math.sqrt(c - i ** 2):
                return True
        return False
