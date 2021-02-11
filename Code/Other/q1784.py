from typing import List


# 从左（右）上角开始根据当前值的大小对r、l的值进行修改
def func(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0:
        return False
    if len(matrix[0]) == 0:
        return False
    r = 0
    l = len(matrix[0]) - 1
    while True:
        print(matrix[r][l] == target)
        if matrix[r][l] == target:
            return True
        elif matrix[r][l] > target:
            if l == 0:
                return False
            l -= 1
        else:
            if r == len(matrix) - 1:
                return False
            r += 1


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]]
    print(func([[1, 1]], 25))
