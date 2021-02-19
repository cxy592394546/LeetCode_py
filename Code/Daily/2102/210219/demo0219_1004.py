from typing import List


def func(A: List[int], K: int) -> int:
    val = 0
    if K == 0:
        l = 0
        for i in range(len(A)):
            if A[i] == 0:
                val = max(val, i - l)
                l = i + 1
        return max(val, len(A) - l)
    B = []
    for i in range(K):
        B.append(0)
    B.append(0)
    z = 0
    for i in range(len(A)):
        if A[i] == 0:
            B[z] = i
            z += 1
            A[i] = 1
        if z == K:
            break
    if z < K:
        return len(A)
    l = 0
    for i in range(len(A)):
        if A[i] == 0:
            val = max(i - B[K], val)
            B[K] = B[z % K] + 1
            B[z % K] = i
            z += 1
    return max(val, len(A) - B[K])


if __name__ == '__main__':
    print(func([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
    # print(func([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
