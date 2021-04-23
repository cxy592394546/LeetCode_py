class Solution:  # KMP
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(haystack) < len(needle):
            return -1
        i, nxt_pos = 0, 0
        flag = True
        while i < (len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if flag and j > 0 and haystack[i + j] == needle[0]:
                    nxt_pos = i + j
                    flag = False
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1 and haystack[i + j] == needle[-1]:
                    return i
            i = nxt_pos if nxt_pos > i else i + 1
        return -1


print(Solution().strStr("hello", "ll"))
