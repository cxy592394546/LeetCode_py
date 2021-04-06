from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = 0
        while i < len(nums):
            if i + 1 != len(nums) and nums[i] == nums[i + 1]:
                while i + 2 != len(nums) and nums[i] == nums[i + 2]:
                    nums.pop(i + 2)
                i += 2
            else:
                i += 1
        return len(nums)


test = Solution()
print(test.removeDuplicates([1, 2, 2, 2]))
