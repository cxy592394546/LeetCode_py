from typing import List


# def func(nums: List[int]) -> List[int]:
#     l1 = len(nums)
#     nums = list(set(nums))
#     l2 = len(nums)
#     for i in range(l1):
#         if i + 1 not in nums:  # list中not in时间复杂度为O(n)
#             nums.append(i + 1)
#     return nums[l2: l1]
def func(nums: List[int]) -> List[int]:
    for i in range(1, len(nums) + 1):
        if nums[i - 1] != 0:
            while nums[i - 1] > 0:
                if nums[nums[i - 1] - 1] == 0:
                    break
                elif nums[i - 1] == i:
                    nums[i - 1] = 0
                else:
                    temp = nums[i - 1]
                    nums[i - 1] = nums[nums[i - 1] - 1]
                    nums[temp - 1] = 0
                print(nums, i)


if __name__ == '__main__':
    print(func([4, 3, 2, 7, 8, 2, 3, 1]))
    print(func([2, 1]))
