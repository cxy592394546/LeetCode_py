from typing import List


def func(A: List[List[int]]) -> List[List[int]]:
    for i in range(len(A)):
        for j in range(len(A[0]) // 2):
            temp = A[i][j]
            A[i][j] = 1 - A[i][len(A[0]) - j - 1]
            A[i][len(A[0]) - j - 1] = 1 - temp
        if len(A[0]) % 2 == 1:
            A[i][len(A[0]) // 2] = 1 - A[i][len(A[0]) // 2]
    return A


if __name__ == '__main__':
    print(func([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
    print(func([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
