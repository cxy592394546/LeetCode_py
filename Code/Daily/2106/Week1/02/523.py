from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        num_set = set()
        pre = 0
        for num in nums:
            last = pre
            pre = (pre + num) % k
            if pre in num_set:
                return True
            num_set.add(last)
        return False
