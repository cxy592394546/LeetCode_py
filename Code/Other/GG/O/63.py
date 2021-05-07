from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_val = prices[0]
        ret = 0
        for price in prices:
            if price < min_val:
                min_val = price
            else:
                ret = max(ret, price - min_val)
        return ret
