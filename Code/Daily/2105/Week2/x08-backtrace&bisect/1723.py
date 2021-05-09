from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def check(limit):
            arr = sorted(jobs)
            groups = [0] * k
            if backtrace(arr, groups, limit):
                return True
            else:
                return False

        def backtrace(arr, groups, limit):
            if not arr:
                return True
            v = arr.pop()
            for i in range(len(groups)):
                if groups[i] + v <= limit:
                    groups[i] += v
                    if backtrace(arr, groups, limit):
                        return True
                    groups[i] -= v
                    # 剪枝，如果这个工人没分到活，那别人肯定得多干活了，那最后的结果必然不是最小的最大值，就不用继续试了。
                    if groups[i] == 0:
                        break
            arr.append(v)
            return False

        l, r = max(jobs), sum(jobs)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
