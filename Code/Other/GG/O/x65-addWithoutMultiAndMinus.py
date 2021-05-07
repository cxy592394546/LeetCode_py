class Solution:
    def add(self, a: int, b: int) -> int:
        mask = 0xffffffff
        a &= mask
        b &= mask
        while b:
            tmp = a ^ b  # 无需 & mask， 因为 a的高位（32位以上，不包括）都为0， b的高位也都为0
            adv = ((a & b) << 1) & mask  # 每一个潜在的运算都要模拟自己在int32的空间中， 主要原因是 << 1 会造成潜在越界。
            a = tmp
            b = adv

        return ~(a ^ mask) if a & (1 << 31) else a