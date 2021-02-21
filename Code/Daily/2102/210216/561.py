from typing import List


def func(nums: List[int]) -> int:
    nums.sort()
    val = 0
    for i in range(0, len(nums), 2):
        val += nums[i]
    return val


if __name__ == '__main__':
    print(func([6, 2, 6, 5, 1, 2]))
