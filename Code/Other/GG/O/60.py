from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        li = [0 for _ in range(n * 6 - n + 1)]
        x = 1
        for i in range(n):
            x *= 6
        li[0] = li[-1] = float('%.5f' % (1 / x))
        li[1] = li[-2] = n * float(li[0])
        rate = 1
        for i in range(n + 1, (7 * n) >> 1):
            li[i] = li[-1 - i] = rate * li[1]
            print(li)
        return li


print(Solution().dicesProbability(1))
