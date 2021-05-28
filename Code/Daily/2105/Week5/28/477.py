from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ret = 0
        for i in range(31):
            cnt = sum(((num >> i) & 1) for num in nums)
            ret += cnt * (len(nums) - cnt)
        return ret