import functools
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        stones_set = set(stones)

        @functools.lru_cache(None)
        def helper(i, step):
            if i == stones[-1]:
                return True

            if i + step + 1 in stones_set:
                if helper(i + step + 1, step + 1):
                    return True

            if i + step in stones_set:
                if helper(i + step, step):
                    return True

            if step > 1 and i + step - 1 in stones_set:
                if helper(i + step - 1, step - 1):
                    return True
            return False
        
        return helper(stones[1], stones[1] - stones[0])


print(Solution().canCross([0, 1, 3, 5, 6, 8, 12, 17]))
print(Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11]))
