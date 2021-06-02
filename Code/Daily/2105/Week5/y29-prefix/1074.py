from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        Row, Col = len(matrix), len(matrix[0])

        presum = [[0 for _ in range(Col + 1)] for _  in range(Row + 1)]
        for r in range(Row):
            for c in range(Col):
                presum[r+1][c+1] = presum[r+1][c] + presum[r][c+1] - presum[r][c] + matrix[r][c]

        res = 0
        for U in range(0, Row + 1):
            for D in range(U + 1, Row + 1):   #2块水平的木板夹住的区域
                section_presum = defaultdict(int)       #2块水平木板中间，矩形右边界从左到右的前缀和
                section_presum[0] = 1
                for c in range(1, Col + 1):
                    prefix = presum[D][c] - presum[U][c]
                    res += section_presum[prefix - target]
                    section_presum[prefix] += 1
        return res


print(Solution().numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))
