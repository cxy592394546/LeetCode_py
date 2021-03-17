from typing import List


def func(matrix: List[List[int]]) -> None:
    if len(matrix) <= 1:
        return matrix
    n = len(matrix)
    for i in range(n):
        for j in range(n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][n - 1 - i]
            matrix[n - 1 - j][n - 1 - i] = temp
    for i in range(n // 2):
        for j in range(n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - i][j]
            matrix[n - 1 - i][j] = temp
    print(matrix)


if __name__ == '__main__':
    print(func([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
