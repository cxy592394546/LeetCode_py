from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[l] <= nums[mid]:
                l = mid
            elif nums[r] >= nums[mid]:
                r = mid
        return


test = Solution()
print(test.findMin([6, 0, 1, 2, 4, 5]))
