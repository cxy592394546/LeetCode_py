from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0 for _ in range(target)]
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        print(dp)
        return dp[-1]


print(Solution().combinationSum4([1, 2, 3, 4, 5], 20))
print(Solution().combinationSum4([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
                                 10))
