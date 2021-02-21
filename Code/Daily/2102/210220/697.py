from typing import List


def func(nums: List[int]) -> int:
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic.keys():
            dic[nums[i]] = [1, i, i]
        else:
            dic[nums[i]][0] += 1
            dic[nums[i]][2] = i
    ret = [0, 0]
    for value in dic.values():
        if value[0] == ret[0]:
            ret[1] = min(ret[1], value[2] - value[1] + 1)
        if value[0] > ret[0]:
            ret[1] = value[2] - value[1] + 1
            ret[0] = value[0]
    return ret[1]


if __name__ == '__main__':
    print(func([1, 2, 2, 3, 1, 4, 2]))
