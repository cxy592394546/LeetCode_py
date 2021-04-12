from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(1, len(nums)):
            for j in range(0, i):
                if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        if nums[0] == 0:
            return "0"
        ret = ""
        for i in range(len(nums)):
            ret += str(nums[i])
        return ret


print(Solution().largestNumber([0, 0]))
print(Solution().largestNumber([3, 30, 34, 5, 9]))
