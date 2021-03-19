from typing import List


def func(matrix: List[List[int]]) -> List[List[int]]:
    ret = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0:
                ret.append([])
            ret[j].append(matrix[i][j])
    return ret


if __name__ == '__main__':
    print(func([[1, 2, 3], [4, 5, 6]]))
