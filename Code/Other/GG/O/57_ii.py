from typing import List
import collections


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l = r = 1
        while sum(range(r)) < target:
            r += 1
        li, ret = [], []
        if sum(range(l, r)) == target:
            ret.append(list(range(l, r)))
        while r != (target >> 1) + 3:
            while sum(range(l, r)) > target:
                l += 1
            print(sum(range(l, r)))
            if sum(range(l, r)) == target:
                ret.append(list(range(l, r)))
            r += 1
        return ret
        
        # 暴力
        # i = 0
        # li, ret = collections.deque([]), []
        # while i != (target >> 1) + 1:
        #     li.append(i + 1)
        #     while sum(li) > target:
        #         li.popleft()
        #     if sum(li) == target:
        #         ret.append(li.copy())
        #     i += 1
        # return ret


print(Solution().findContinuousSequence(15))
