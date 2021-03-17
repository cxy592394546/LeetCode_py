class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S) < 2:
            return S
        i = 0
        while i <= len(S):
            if i + 1 < len(S):
                while S[i] == S[i + 1]:
                    S = S[:i] + S[i + 2:]
                    i = i - 1 if i > 0 else 0
                    if len(S) < 2 or i + 2 > len(S):
                        return S
            i += 1
        return S


test = Solution()
print(test.removeDuplicates("ibfjcaffccadidiaidchakchchcahabhibdcejkdkfbaeeaecdjhajbkfebebfea"))
