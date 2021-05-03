class Solution:
    def reverse(self, x: int) -> int:
        flag = True
        if x < 0:
            flag = False
            s = str(x)[1:]
        else:
            s = str(x)
        if len(s) == 1:
            return x
        s = s[::-1]
        tmp = s[-1]
        if int(s[:-1]) > (2 ** 31 // 10):
            return 0
        elif int(s[:-1]) == (2 ** 31 // 10):
            if flag:
                return int(s) if int(tmp) <= 7 else 0
            else:
                return int("-" + s) if int(tmp) <= 8 else 0
        else:
            return int(s) if flag else int("-" + s)


print(Solution().reverse(-1463847412))