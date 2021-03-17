from typing import List


def __init__(self, matrix: List[List[int]]):
    self.matrix = matrix
    if len(matrix) == 0 or len(matrix[0]) == 0:
        matrix = [[0]];
    else:
        for i in range(1, len(matrix)):
            matrix[i][0] += matrix[i - 1][0]
        for i in range(1, len(matrix[0])):
            matrix[0][i] += matrix[0][i - 1]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1] + matrix[i][j]


def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    matrix = self.matrix
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0;
    if row1 == 0 and col1 == 0:
        return matrix[row2][col2]
    elif row1 == 0:
        return matrix[row2][col2] - matrix[row2][col1 - 1]
    elif col1 == 0:
        return matrix[row2][col2] - matrix[row1 - 1][col2]
    else:
        return matrix[row2][col2] - matrix[row1 - 1][col2] - matrix[row2][col1 - 1] + matrix[row1 - 1][col1 - 1]
