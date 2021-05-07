from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        dp = [0] * (max(nums) + 1)
        for val in nums:
            dp[val] += val
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + dp[i], dp[i - 1])
        return dp[-1]


print(Solution().deleteAndEarn(nums=[3, 4, 2]))
