from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix = [0 for _ in range(len(arr) + 1)]
        ret = 0
        for i in range(n := len(arr)):
            prefix[i + 1] = prefix[i] ^ arr[i]
        for i in range(n):
            for j in range(i + 1, n + 1):
                #   如果两点间亦或和为0则这两点间任取一点其两侧值必相等
                if prefix[i] == prefix[j]:
                    ret += j - i - 1
        return ret
