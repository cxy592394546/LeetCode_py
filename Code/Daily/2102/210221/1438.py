from typing import List
from sortedcontainers import SortedList


def func(nums: List[int], limit: int) -> int:
    s = SortedList()
    n = len(nums)
    left = right = ret = 0

    while right < n:
        s.add(nums[right])
        while s[-1] - s[0] > limit:
            s.remove(nums[left])
            left += 1
        ret = max(ret, right - left + 1)
        right += 1

    return ret


if __name__ == '__main__':
    print(func([8, 2, 4, 7], 4))
