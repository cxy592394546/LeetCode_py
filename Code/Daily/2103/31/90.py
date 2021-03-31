from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = [[]]
        self.makeList(ret, nums)
        return ret

    def makeList(self, ret, cur):
        if not cur:
            return
        i, right = 0, 0
        item = ret[-1]
        while i != len(cur):
            ret.append(item + [cur[i]])
            self.makeList(ret, cur[i + 1:])
            while right != len(cur) and cur[i] == cur[right]:
                right += 1
            i = right


test = Solution()
print(test.subsetsWithDup([1, 2, 2]))
