from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target == matrix[0][0] or target == matrix[-1][-1]:
            return True
        if len(matrix) * len(matrix[0]) == 1:
            return target == matrix[0][0]
        return self.search(matrix, 0, len(matrix) * len(matrix[0]) - 1, target)

    def search(self, matrix, i, j, target):
        if i == j - 1:
            return False
        mid = int((i + j) / 2)
        if target == matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
            return True
        elif target >= matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
            return self.search(matrix, mid, j, target)
        elif target <= matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
            return self.search(matrix, i, mid, target)
        return False


test = Solution()
print(test.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60))
print(test.searchMatrix([[1]], 0))
