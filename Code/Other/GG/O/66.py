from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if len(a) == 0:
            return []
        if len(a) == 1:
            return [1]
        li1, li2 = [a[0]] + [0 for _ in range(len(a) - 2)], [a[-1]] + [0 for _ in range(len(a) - 2)]
        for i in range(1, len(a) - 1):
            li1[i] = li1[i - 1] * a[i]
            li2[i] = li2[i - 1] * a[len(a) - i - 1]
        li1 = [1] + li1
        li2 = [1] + li2
        for i in range(len(li1)):
            li1[i] *= li2[-i - 1]
        return li1


print(Solution().constructArr([1, 2, 3, 4, 5]))
