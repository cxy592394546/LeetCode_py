from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        num = 0
        for item in nums:
            num ^= item
        li = num & -num
        ret = [0, 0]
        for item in nums:
            if item & li == li:
                ret[0] ^= item
            else:
                ret[1] ^= item
        return ret


print(Solution().singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))
print(Solution().singleNumbers([4, 1, 4, 6]))
