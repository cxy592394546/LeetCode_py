class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dic = dict()
        ret = []
        nums.sort()
        for i in range(len(nums)):
            cur = [nums[i]]
            for k, v in dic.items():
                if nums[i] % k == 0:
                    if len(v) >= len(cur):
                        cur = v.copy()
                        cur.append(nums[i])
            dic[nums[i]] = cur
            ret = cur if len(cur) > len(ret) else ret
        return ret