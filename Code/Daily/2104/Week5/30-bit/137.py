# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         bit = [0 for _ in range(32)]
#         i = 0
#         for num in nums:
#             while num != 0:
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit = [0 for _ in range(32)]
        i = 0
        for num in nums:
            if num < 0:
                bit[31] += 1
                num = -num
            while num != 0:
                bit[i] += num % 2
                num >>= 1
                i += 1
            i = 0
        ret = 0
        print(bit)
        for i in range(30, -1, -1):
            ret *= 2
            if bit[i] % 3 != 0:
                ret += 1
        if ret == 0 and bit[31] % 3 != 0:
            return -2147483648
        return ret if bit[31] % 3 == 0 else -ret


print(Solution().singleNumber([2, -1, 2, 2]))
