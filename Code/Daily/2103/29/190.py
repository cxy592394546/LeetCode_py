class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            ret += (n % 2) << (31 - i)
            n //= 2
        return ret
