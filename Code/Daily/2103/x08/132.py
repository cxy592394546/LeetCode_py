class Solution:
    def func(self, s: str) -> int:  # 动态规划
        # n = len(s)
        # g = [[True] * n for _ in range(n)]
        #
        # for i in range(n - 1, -1, -1):
        #     for j in range(i + 1, n):
        #         g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]
        #
        # f = [float("inf")] * n
        # for i in range(n):
        #     if g[0][i]:
        #         f[i] = 0
        #     else:
        #         for j in range(i):
        #             if g[j + 1][i]:
        #                 f[i] = min(f[i], f[j] + 1)
        #
        # return f[n - 1]
        if s == s[::-1] or len(s) < 2:
            return 0

        ret = [float("inf")] * len(s)
        for i in range(1, len(s) + 1):
            if s[:i] == s[(i - 1)::-1]:
                ret[i - 1] = 0
            else:
                for j in range(1, i):
                    if s[j:i] == s[i - 1:j - 1:-1]:
                        ret[i - 1] = min(ret[i - 1], ret[j - 1] + 1)
                        print(ret)

        return ret[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.func("aabbad"))
