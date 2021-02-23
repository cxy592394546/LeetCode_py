from typing import List


def func(matrix: List[List[int]]) -> bool:
    r, c = 0, len(matrix) - 2
    if len(matrix) == 1 or len(matrix[0]) == 1:
        return True
    while r != len(matrix[0]) and c >= 0:
        val = matrix[c][r]
        x, y = r, c
        while y < len(matrix) and x < len(matrix[0]):
            print(x, y, matrix[y][x])
            if val != matrix[y][x]:
                return False
            y += 1
            x += 1
        c -= 1
    r = c = 0
    while r < len(matrix[0]):
        print(r)
        val = matrix[c][r]
        x, y = r, c
        while y < len(matrix) and x < len(matrix[0]):
            print(x, y, matrix[y][x])
            if val != matrix[y][x]:
                return False
            y += 1
            x += 1
        r += 1
    return True


if __name__ == '__main__':
    # print(func([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
    # print(func([[1, 2], [2, 2]]))
    print(func([[11, 74, 0, 93], [40, 11, 74, 7]]))
