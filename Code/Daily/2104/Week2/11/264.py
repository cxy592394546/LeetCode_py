class Solution:
    def nthUglyNumber(self, n: int) -> int:
        li = [1 for _ in range(n)]
        a = b = c = 0
        for i in range(1, n):
            li[i] = min(li[a] * 2, min(li[b] * 3, li[c] * 5))
            if li[a] * 2 == li[i]:
                a += 1
            if li[b] * 3 == li[i]:
                b += 1
            if li[c] * 5 == li[i]:
                c += 1
        return li[-1]
        # a, b, c = [1], [1], [1]
        # a_pos, b_pos, c_pos = 0, 0, 0
        # while len(a) != n:
        #     if a[a_pos] * 2 == min(a[a_pos] * 2, min(b[b_pos] * 3, c[c_pos] * 5)):
        #         a.append(a[a_pos] * 2)
        #         b.append(a[a_pos] * 2)
        #         c.append(a[a_pos] * 2)
        #         a_pos += 1
        #     elif b[b_pos] * 3 == min(a[a_pos] * 2, min(b[b_pos] * 3, c[c_pos] * 5)):
        #         a.append(b[b_pos] * 3)
        #         b.append(b[b_pos] * 3)
        #         c.append(b[b_pos] * 3)
        #         b_pos += 1
        #     elif c[c_pos] * 5 == min(a[a_pos] * 2, min(b[b_pos] * 3, c[c_pos] * 5)):
        #         a.append(c[c_pos] * 5)
        #         b.append(c[c_pos] * 5)
        #         c.append(c[c_pos] * 5)
        #         c_pos += 1
        #     if b[b_pos] * 3 == b[-1]:
        #         b_pos += 1
        #     if c[c_pos] * 5 == c[-1]:
        #         c_pos += 1
        # return a[-1]