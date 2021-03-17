from typing import List


class Solution:
    @staticmethod
    def func(matrix: List[List[int]]) -> List[int]:
        l, r, u, d = 0, len(matrix[0]), 0, len(matrix)
        ret = []
        while True:
            for i in range(l, r):
                ret.append(matrix[u][i])
            u += 1
            if l == r or u == d:
                return ret
            for i in range(u, d):
                ret.append(matrix[i][r - 1])
            r -= 1
            if l == r or u == d:
                return ret
            for i in range(r - 1, l - 1, -1):
                ret.append(matrix[d - 1][i])
            d -= 1
            if l == r or u == d:
                return ret
            for i in range(d - 1, u - 1, -1):
                ret.append(matrix[i][l])
            l += 1
            if l == r or u == d:
                return ret
        return ret


test = Solution()
print(test.func([[1]]))
print(test.func([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
