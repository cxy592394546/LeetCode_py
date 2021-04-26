from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        start, end = max(weights), sum(weights)
        if D == 1:
            return end
        while start <= end:
            if start == end:
                return start
            mid = (start + end) >> 1
            days = self.findMinDay(weights, mid)
            if days > D:
                start = mid + 1
            elif days <= D:
                end = mid

    def findMinDay(self, weights, m_weight):
        ret, cur = 0, 0
        for item in weights:
            if cur + item > m_weight:
                cur, ret = 0, ret + 1
            cur += item
        return ret + 1


print(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
