class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dic = dict()
        ret = []
        for num in nums:
            li = []
            for key, val in dic.items():
                if num % key == 0 and len(val) > len(li):
                    li = val
            if not li:
                dic[num] = [num]
            else:
                dic[num] = li + [num]
            if len(dic[num]) > len(ret):
                ret = dic[num]
        return ret