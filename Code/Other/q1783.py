from typing import List


def func(nums: List[int]) -> int:
    nums.sort()
    for i in range(0, len(nums)):
        if nums[i] == nums[i + 1]:
            return nums[i]


if __name__ == '__main__':
    print(func([2, 3, 8, 4, 3, 2]))
