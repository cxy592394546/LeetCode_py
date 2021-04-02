from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        hi, hist, li = 0, 0, []
        ret = 0
        for i, item in enumerate(height):
            if hi == 0 and item == 0:
                continue
            if item >= hi:
                for n in li:
                    ret += n
                hi = item
                hist = i
                li = []
            else:
                li.append(hi - item)
        hi, li = 0, []
        for i in range(len(height) - 1, hist - 1, -1):
            if hi == 0 and height[i] == 0:
                continue
            if height[i] >= hi:
                for n in li:
                    ret += n
                hi = height[i]
                li = []
            else:
                li.append(hi - height[i])
        return ret


test = Solution()
print(test.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(test.trap([1, 1, 0, 2]))
