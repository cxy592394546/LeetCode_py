from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        ret = [0 for _ in range(len(encoded) + 1)]
        for i in range(1, len(encoded) + 2):
            ret[0] ^= i
        for i in range(1, len(encoded), 2):
            ret[0] ^= encoded[i]
        for i in range(1, len(ret)):
            ret[i] = ret[i - 1] ^ encoded[i - 1]
        return ret


print(Solution().decode(encoded=[12, 6, 11, 10, 5, 3, 4, 6]))
