from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        li = [1/6 for _ in range(6)]
        for i in range(2, n + 1):
            tmp = [0 for _ in range(5 * i + 1)]
            for j in range(len(li)):
                for k in range(6):
                    tmp[j + k] += li[j] / 6
            li = tmp
        return li


print(Solution().dicesProbability(3))
