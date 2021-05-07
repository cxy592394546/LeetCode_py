from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret = [first] + [0 for _ in range(len(encoded))]
        for i in range(len(encoded)):
            ret[i + 1] = encoded[i] ^ ret[i]
        return ret


print(Solution().decode(encoded=[6, 2, 7, 3], first=4))
