from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(first, end):
            cur, pre = max(nums[first + 1], nums[first]), nums[first]
            for i in range(first + 2, end + 1):
                pre, cur = cur, max(pre + nums[i], cur)
            return cur

        if len(nums) < 3:
            return max(nums[0], nums[-1])
        return max(helper(0, len(nums) - 2), helper(1, len(nums) - 1))
