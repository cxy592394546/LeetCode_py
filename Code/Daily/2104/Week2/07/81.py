from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        if nums[0] == target or nums[-1] == target:
            return True
        l, r = 0, len(nums) - 1
        while 0 <= l < len(nums) and nums[l] == nums[0]:
            l += 1
        while l <= r and nums[r] == nums[0]:
            r -= 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

