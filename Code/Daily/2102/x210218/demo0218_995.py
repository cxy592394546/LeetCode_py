from typing import List


def func(A: List[int], K: int) -> int:
    counter = 0
    B = []  # i + K位置处标记
    C = 0  # 前一位变化次数
    for i in range(K):
        B.append(0)
    for i in range(len(A)):
        if A[i] == 0:
            B[i % K] = 1
            C += 1
        elif A[i] == 1:
            B[i % K] = 0
        if (A[i] + B[i % K] + C) % 2 == 0:
            if i + K >= len(A):
                return -1
            counter += 1
    return counter
    # for i in range(len(A) - K + 1):
    #     if A[i] == 0:
    #         for j in range(K):
    #             A[i + j] = 1 - A[i + j]
    #         counter += 1
    # for i in range(K):
    #     if A[-1 - i] == 0:
    #         return -1
    # return counter


if __name__ == '__main__':
    print(func([0, 0, 0, 1, 0, 1, 1, 0], 3))
