from typing import List


def func(nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    n = len(nums) * len(nums[0])
    if r * c != n:
        return nums
    counter_r, counter_c = 0, 0
    val = [[]]
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if counter_c == c:
                counter_c = 0
                counter_r += 1
                val.append([])
            val[counter_r].append(nums[i][j])
            counter_c += 1
    return val


if __name__ == '__main__':
    print(func([[4, 3], [2, 1]], 1, 4))
