from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or nums[-1] < target or nums[0] > target:
            return 0
        ret = 0
        if nums[0] == target and nums[-1] == target:
            return len(nums)
        elif nums[0] == target:
            l, r, ret = 0, 1, 0
        elif nums[-1] == target:
            l, r, ret = len(nums) - 2, len(nums) - 1, 0
        else:
            l, r = 0, len(nums) - 1
            mid = (l + r) // 2
            while l <= r:
                if nums[mid] == target:
                    pos = mid
                    l, r, ret = pos - 1, pos + 1, 1
                    break
                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                mid = (l + r) // 2
        while l > -1 and r < len(nums):
            if nums[l] != target and nums[r] != target:
                return ret
            else:
                if nums[l] == target:
                    if l != 0:
                        l -= 1
                    else:
                        nums[l] += 1
                    ret += 1
                if nums[r] == target:
                    if r != len(nums) - 1:
                        r += 1
                    else:
                        nums[r] += 1
                    ret += 1
                if l == 0 and r == len(nums) - 1:
                    return ret
        return ret


test = Solution()
print(test.search([1, 8, 8], 8))
