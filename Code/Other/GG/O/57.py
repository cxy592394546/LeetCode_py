import sys
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        revs = set()
        for num in nums:
            if num not in revs:
                revs.add(target - num)
            else:
                return [num, target - num]

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     l, r = 0, len(nums) - 1
    #     while l <= r:
    #         if nums[l] + nums[r] == target:
    #             return [nums[l], nums[r]]
    #         elif nums[l] + nums[r] > target:
    #             r -= 1
    #         elif nums[l] + nums[r] < target:
    #             l += 1
