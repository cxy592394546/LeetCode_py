class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) <= len(t) and s != t:
            return 0
        if len(s) == 0 and len(t) == 0:
            return 1
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if i < j:
                    continue
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(s)][len(t)]
