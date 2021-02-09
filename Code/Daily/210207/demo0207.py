from typing import List


def func(nums: List[int]) -> bool:
    flag = False
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if flag is False:
                if i == 0 or i + 2 == len(nums):
                    flag = True
                else:
                    if nums[i - 1] > nums[i + 1]:
                        if nums[i] < nums[i + 2]:
                            flag = True
                        else:
                            return False
                    else:
                        flag = True
            else:
                return False
    return True


if __name__ == '__main__':
    print(func([5, 7, 1, 8]))
