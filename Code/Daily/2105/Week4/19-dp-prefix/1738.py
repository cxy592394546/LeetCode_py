from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dp[0][0] = matrix[0][0]
        li = [matrix[0][0]]
        for i in range(1, r := len(dp)):
            dp[i][0] = dp[i - 1][0] ^ matrix[i][0]
            li.append(dp[i][0])
        for i in range(1, c := len(dp[0])):
            dp[0][i] = dp[0][i - 1] ^ matrix[0][i]
            li.append(dp[0][i])
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = dp[i - 1][j] ^ dp[i][j - 1] ^ dp[i - 1][j - 1]
                li += [dp[i][j]]
        li.sort()
        print(li)
        return li[-k]


print(Solution().kthLargestValue([[5, 2], [1, 6], [3, 4]], 1))
