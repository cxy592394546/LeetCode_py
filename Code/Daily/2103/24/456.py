from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack, _Min = [], -float("inf")
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < _Min:
                return True
            while stack and nums[i] > stack[-1]:
                _Min = stack.pop()
            stack.append(nums[i])
        return False


test = Solution()
print(test.find132pattern([-1, 4, 4, 0]))
