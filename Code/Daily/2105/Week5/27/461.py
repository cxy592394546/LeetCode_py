class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        while x > 0 or y > 0:
            if x & -x == y & -y:
                x -= x & -x
                y -= y & -y
            elif (x == 0 or x & -x > y & -y) and y != 0:
                cnt += 1
                y -= y & -y
            elif y == 0 or x & -x < y & -y:
                cnt += 1
                x -= x & -x
        return cnt


print(Solution().hammingDistance(3, 1))
