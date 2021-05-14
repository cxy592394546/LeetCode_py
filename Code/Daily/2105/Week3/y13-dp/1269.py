class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        #  动态规划(递归法超时)
        columns = min(steps // 2 + 1, arrLen)
        dp = [[0 for _ in range(columns + 1)] for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(columns):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1]
                if j < columns - 1:
                    dp[i][j] += dp[i - 1][j + 1]
                dp[i][j] %= (1000000000 + 7)
        return dp[-1][0]


print(Solution().numWays(5, 6))
