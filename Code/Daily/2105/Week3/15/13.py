class Solution(object):
    def romanToInt(self, s):
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum_val = 0
        for i in range(len(s) - 1):
            if d[s[i]] < d[s[i + 1]]:
                sum_val -= d[s[i]]
            else:
                sum_val += d[s[i]]
        sum_val += d[s[-1]]

        return sum_val
