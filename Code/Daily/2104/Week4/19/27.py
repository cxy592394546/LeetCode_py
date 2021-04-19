from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        l, r = 0, len(nums) - 1
        while True:
            while l != len(nums) and nums[l] != val:
                l += 1
            while r != -1 and nums[r] == val:
                r -= 1
            if r <= l:
                return r + 1
            nums[l] = nums[r]
            r -= 1
