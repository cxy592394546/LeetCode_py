from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        ret = [False for _ in range(len(queries))]
        prefix = [candiesCount[0] for _ in range(len(candiesCount))]
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + candiesCount[i]
        for i in range(len(queries)):
            if queries[i][0] == 0:
                ret[i] = candiesCount[0] > queries[i][1]
            elif queries[i][0] != 0:
                ret[i] = (prefix[queries[i][0] - 1] < (queries[i][1] + 1) * queries[i][2] and prefix[queries[i][0]] > queries[i][1])
        return ret