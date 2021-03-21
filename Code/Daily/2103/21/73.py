from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:  # 首行列置1
        row0, col0 = False, False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0 = True
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                row0 = True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0
        if col0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if row0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0


test = Solution()
# print(test.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(test.setZeroes([[0]]))
