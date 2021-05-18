from typing import List


def func(nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] not in dic.keys():
            dic[nums[i]] = i
        else:
            return [dic[target - nums[i]], i]
    return []


if __name__ == '__main__':
    print(func([2, 7, 11, 15], 9))
