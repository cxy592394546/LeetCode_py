from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        max_val, min_val = max(bloomDay), 0
        while max_val > min_val:
            mid = (max_val + min_val) >> 1
            i, counter, sum_m = 0, 0, 0
            while i < len(bloomDay) - k + 1:
                while k != counter:
                    if bloomDay[i] <= mid:
                        i += 1
                        counter += 1
                    else:
                        i += 1
                        break
                if counter == k:
                    sum_m += 1
                counter = 0
                if sum_m == m:
                    break
            if sum_m == m:
                max_val = mid
            elif sum_m < m:
                min_val = mid + 1
        return min_val


print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))
