from typing import List


def func(matrix: List[List[int]], target: int) -> bool:
    r = l = 0
    for i in range(0, len(matrix)):
        if matrix[i][0] > target:
            r = i
            break
        elif matrix[i][0] == target:
            return True
    for i in range(0, len(matrix[0])):
        if matrix[0][i] > target:
            xl = i
            break
        elif matrix[0][i] == target:
            return True
    print(r, l)


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]]
    print(func(matrix, 5))
