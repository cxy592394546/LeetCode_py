import bisect
from typing import List


def func(envelopes: List[List[int]]) -> int:  # 最长子序列 + 二分查找
    if len(envelopes) == 0:
        return 0

    envelopes.sort(key=lambda x: (x[0], -x[-1]))
    print(envelopes)

    ret = [envelopes[0][1]]
    for i in range(1, len(envelopes)):
        if envelopes[i][1] > ret[-1]:
            ret.append(envelopes[i][-1])
        else:
            index = bisect.bisect_left(ret, envelopes[i][1])
            ret[index] = envelopes[i][1]
    return len(ret)


if __name__ == '__main__':
    # print(func([[5, 4], [6, 4], [6, 7], [2, 3]]))
    print(func([[19, 17], [8, 14], [11, 4], [12, 20], [19, 13], [3, 12], [5, 12], [19, 9], [20, 3], [11, 19], [20, 20],
                [7, 14], [9, 13], [2, 8], [20, 7], [16, 6], [16, 3], [10, 2], [4, 6], [3, 17]]))
