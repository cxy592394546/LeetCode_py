from typing import List


def __init__(self, nums: List[int]):    #   前缀和法
    self.sums = []
    _sums = self.sums
    _sums.append(0)
    for i in range(0, len(nums)):
        _sums.append(_sums[i] + nums[i])

def sumRange(self, i: int, j: int) -> int:
    _sums = self.sums
    return _sums[j + 1] - _sums[i]

# 暴力
# def __init__(self, nums: List[int]):
#     self.nums = nums
#
# def sumRange(self, i: int, j: int) -> int:
#     return sum(self.nums[i:j + 1])
