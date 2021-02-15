from typing import List


def func(nums: List[int]) -> int:
    cnt = 0
    res = 0
    for num in nums:
        if num == 1:
            cnt += 1
            res = max(res, cnt)
        else:
            cnt = 0
    return res


if __name__ == '__main__':
    print(func([1, 1, 0, 1]))
