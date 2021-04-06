from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == mid:
                if mid == len(nums) - 1 or nums[mid + 1] != mid + 1:
                    return mid + 1
                l = mid + 1
            else:
                if mid == 0 or nums[mid - 1] == mid - 1:
                    return mid
                r = mid - 1


test = Solution()
print(test.missingNumber([1]))
