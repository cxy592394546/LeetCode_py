class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        li = s.split()
        ret = ''
        for i in range(len(li)):
            ret += li[len(li) - i - 1] + ' '
        return ret.strip()