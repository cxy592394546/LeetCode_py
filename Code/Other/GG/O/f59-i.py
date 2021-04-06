from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        li, ret = [], []
        for i in range(k):
            while li and nums[i] >= nums[li[-1]]:
                li.pop()
            li.append(i)
        for i in range(k, len(nums)):
            if li[0] == i - k:
                li.pop(0)
            while li and nums[i] >= nums[li[-1]]:
                li.pop()
            li.append(i)
            ret.append(nums[li[0]])
        return ret

        # if len(nums) == 0:
        #     return []
        # if len(nums) == 1:
        #     return [nums[0]]
        # if k == 1:
        #     return nums
        # li, ret = [], []
        # for i in range(k):
        #     li.append(nums[i])
        # li = sorted(li, key=lambda x: x)
        # ret.append(li[-1])
        # for i in range(k, len(nums)):
        #     li.remove(nums[i - k])
        #     for j in range(k - 1):
        #         if nums[i] < li[j]:
        #             li.insert(j, nums[i])
        #             break
        #         if j == k - 2:
        #             li.append(nums[i])
        #     ret.append(li[-1])
        # return ret


test = Solution()
print(test.maxSlidingWindow([3, 1, 2, 1, 0, 1, 7, 6], 3))
print(test.maxSlidingWindow([1, -1], 1))
