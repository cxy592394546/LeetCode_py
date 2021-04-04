from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if len(answers) == 0:
            return 0
        ret = 0
        dic = {}
        for item in answers:
            if item == 0:
                ret += 1
                continue
            if item not in dic:
                dic[item] = 1
            elif item in dic:
                if dic[item] == item:
                    ret += item + 1
                    del dic[item]
                else:
                    dic[item] += 1
        for key in dic.keys():
            ret += key + 1
        return ret
