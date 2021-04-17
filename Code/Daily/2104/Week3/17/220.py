from bisect import bisect_left
from typing import List
from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0:
            return t == 0
        val_li = SortedList()
        left = 0
        for i, val in enumerate(nums):
            if i - left > k:
                val_li.remove(nums[left])
                left += 1
            index = bisect_left(val_li, val - t)  # ?
            print(index, val_li)
            if val_li and index < len(val_li) and (abs(val_li[index] - val) <= t or abs(val_li[index - 1] - val) <= t):
                return True
            val_li.add(val)
        return False


print(Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
