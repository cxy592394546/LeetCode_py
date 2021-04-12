from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(num1, num2):
            if str(num1) + str(num2) > str(num2) + str(num1):
                return -1
            else:
                return 1
        nums.sort(key=cmp_to_key(compare))
        print(nums)
        if nums[0] == 0:
            return "0"
        ret = ""
        for i in range(len(nums)):
            ret += str(nums[i])
        return ret


print(Solution().largestNumber([0, 0]))
print(Solution().largestNumber([3, 30, 34, 5, 9]))
