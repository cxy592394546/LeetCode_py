def func(s: str, t: str, maxCost: int) -> int:  # 超时
    cost = []
    for i in range(0, len(s)):
        cost.append(abs(ord(s[i]) - ord(t[i])))
    bgn = 0
    val = 0
    m_val = 0
    temp_cost = 0
    while bgn + val != len(s):
        if temp_cost + cost[bgn + val] <= maxCost:
            temp_cost += cost[bgn + val]
            val += 1
            if val > m_val:
                m_val = val
        else:
            if val > m_val:
                m_val = val
            if cost[bgn + val] > maxCost:
                bgn += val + 1
                val = 0
                temp_cost = 0
            else:
                for i in range(0, val):
                    if temp_cost + cost[bgn + val] > maxCost:
                        temp_cost -= cost[bgn]
                        bgn += 1
                        val -= 1
                temp_cost += cost[bgn + val]
                val += 1
    return m_val


def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    n = len(s)
    used = 0
    max_size = 0
    l, r = 0, 0
    while r <n:
        cost = abs(ord(s[r])-ord(t[r]))
        used += cost
        if used > maxCost:
            used -= abs(ord(s[l])-ord(t[l]))
            l += 1
        size = r-l+1
        max_size = max(max_size, size)
        r += 1
    return max_size


if __name__ == '__main__':
    s = "abcd"
    t = "zcde"
    print(func(s, t, 3))
