from typing import List


class Solution:  # 回溯法
    def func(self, s: str) -> List[List[str]]:
        ret = []
        self.backtrack(s, ret, [])
        return ret

    def backtrack(self, s, ret, pre):
        if len(s) == 0:
            ret.append(pre)
        else:
            for i in range(len(s)):
                if s[:i + 1] == s[i:: -1]:
                    self.backtrack(s[i + 1:], ret, pre + [s[:i + 1]])


if __name__ == '__main__':
    solution = Solution()
    print(solution.func("asdfdfdsa"))
