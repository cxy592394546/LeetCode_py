from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        ret = [[0 for _ in range(n)] for _ in range(n)]
        u, d, l, r = 0, n, 0, n
        count = 1
        while True:
            for i in range(l, r):
                ret[u][i] = count
                count += 1
            u += 1
            if u == d:
                break
            for i in range(u, d):
                ret[i][r - 1] = count
                count += 1
            r -= 1
            if l == r:
                break
            for i in range(r - 1, l - 1, -1):
                ret[d - 1][i] = count
                count += 1
            d -= 1
            if u == d:
                break
            for i in range(d - 1, u - 1, -1):
                ret[i][l] = count
                count += 1
            l += 1
            if l == r:
                break
        return ret


test = Solution()
print(test.generateMatrix(3))
