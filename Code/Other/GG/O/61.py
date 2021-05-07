from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        num = set()
        max_val, min_val = 0, 14
        for i in range(nums):
            if nums[i] != 0:
                if nums[i] not in num:
                    num.add(nums[i])
                    max_val = max(max_val, nums[i])
                    min_val = min(min_val, nums[i])
                else:
                    return False
        return max_val - min_val < 5
        # nums.sort()
        # num = i = 0
        # while i < len(nums) and nums[i] == 0:
        #     num += 1
        #     i += 1
        #     if i == len(nums) - 1:
        #         return True
        # if nums[-1] - nums[i] > 4:
        #     return False
        # for j in range(i, 5):
        #     if nums[j] == nums[j - 1]:
        #         return False
        # return True
        # return len(nums[i:]) == len(set(nums[i:]))


print(Solution().isStraight([0, 0, 0, 0, 0]))
