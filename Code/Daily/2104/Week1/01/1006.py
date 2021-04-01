class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1
        elif N == 2:
            return 2
        elif N == 3:
            return 6
        elif N == 4:
            return 7
        ret = 0
        flag = True
        while N > 3:
            if flag:
                ret += N * (N - 1) // (N - 2) + (N - 3)
                N -= 4
                flag = False
            else:
                ret -= N * (N - 1) // (N - 2) - (N - 3)
                N -= 4
        if N == 1:
            return ret - 1
        elif N == 2:
            return ret - 2
        elif N == 3:
            return ret - 6
        return ret