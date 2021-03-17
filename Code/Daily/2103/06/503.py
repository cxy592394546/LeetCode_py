from typing import List


def func(nums: List[int]) -> List[int]:
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [-1]
    ret = []
    tmp = []
    n = len(nums)
    for i in range(n):
        ret.append(-1)
        while len(tmp) > 0 and nums[i] > tmp[-1][1]:
            if nums[i] > tmp[-1][1]:
                ret[tmp[-1][0]] = nums[i]
                tmp.pop()
        tmp.append([i, nums[i]])
    for i in range(tmp[0][0] + 1):
        nums.append(nums[1])
        while len(tmp) > 0 and nums[i] > tmp[-1][1]:
            if nums[i] > tmp[-1][1]:
                ret[tmp[-1][0]] = nums[i]
                tmp.pop()
    return ret


if __name__ == '__main__':
    print(func([3, 2, 1]))
