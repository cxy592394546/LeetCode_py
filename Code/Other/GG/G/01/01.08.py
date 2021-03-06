from typing import List


def func(matrix: List[List[int]]) -> None:
    if len(matrix) == 0 and len(matrix[0]) == 0:
        return matrix
    dic = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if 'r' not in dic.keys():
                    dic['r'] = [i]
                    dic['c'] = [j]
                else:
                    if i not in dic['r']:
                        dic['r'].append(i)
                    if j not in dic['c']:
                        dic['c'].append(j)
    for r in dic['r']:
        for c in range(len(matrix[0])):
            matrix[r][c] = 0
    for c in dic['c']:
        for r in range(len(matrix)):
            matrix[r][c] = 0

    print(matrix)


if __name__ == '__main__':
    print(func([
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]))
