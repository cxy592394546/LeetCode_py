from functools import reduce
from operator import xor
from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return len(nums) % 2 == 0 or reduce(xor, nums) == 0


print(Solution().xorGame([1, 2, 1]))
