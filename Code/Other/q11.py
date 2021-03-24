from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        self.max = min(height[0], height[-1]) * (len(height) - 1)
        return self.findMax(height)

    def findMax(self, height):
        left, right = 0, len(height) - 1
        while left < right:
            while left != right and height[left] > height[left + 1]:
                left += 1
            while left != right and height[right] > height[right - 1]:
                right -= 1
            if left == right:
                return max(self.max, min(height[left], height[right]) * (right - left))
            else:
                self.max = max(self.max, min(height[left], height[right]) * (right - left),
                               min(height[0], height[right]) * (right - 0),
                               min(height[left], height[0]) * (len(height) - 1 - left))
                return self.findMax(height[left:right + 1])


test = Solution()
print(test.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
