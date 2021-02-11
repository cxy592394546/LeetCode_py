import collections
from typing import List


# K个 - K-1个
def func(A: List[int], K: int) -> int:
    n = len(A)
    num1, num2 = collections.Counter(), collections.Counter()
    tot1 = tot2 = 0
    left1 = left2 = right = 0
    ret = 0

    for right, num in enumerate(A):
        if num1[num] == 0:
            tot1 += 1
        num1[num] += 1
        if num2[num] == 0:
            tot2 += 1
        num2[num] += 1

        while tot1 > K:
            num1[A[left1]] -= 1
            if num1[A[left1]] == 0:
                tot1 -= 1
            left1 += 1
        while tot2 > K - 1:
            num2[A[left2]] -= 1
            if num2[A[left2]] == 0:
                tot2 -= 1
            left2 += 1

        ret += left2 - left1

    return ret
