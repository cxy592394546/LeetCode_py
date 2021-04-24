from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        bits = [0 for _ in range(32)]
        for num in nums:
            i = 0
            while num > 0:
                bits[i] += num % 2
                num >>= 1
                i += 1
        print(bits)
        for i in range(31, -1, -1):
            ret <<= 1
            if bits[i] % 3 != 0:
                ret += 1
        return ret


print(Solution().singleNumber([3, 3, 3, 4]))
