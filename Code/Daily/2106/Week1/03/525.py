class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: -1}
        counter, ret = 0, 0
        for i, num in enumerate(nums):
            if num == 1:
                counter += 1
            else:
                counter -= 1
            if counter in dic.keys():
                ret = max(ret, i - dic[counter])
            else:
                dic[counter] = i
        return ret
