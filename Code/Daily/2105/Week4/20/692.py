from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = dict()
        for item in words:
            if item not in counter:
                counter[item] = 1
            else:
                counter[item] += 1
        ret = []
        counter = sorted(counter.items(), key=lambda item: (item[1], item[0]), reverse=True)
        pos = 0
        for i in range(len(counter)):
            if i + 1 < len(counter) and counter[i + 1][1] == counter[pos][1]:
                continue
            else:
                ret += counter[i:None if pos == 0 else pos - 1:-1]
                pos = i + 1
                print(counter, ret)
            if len(ret) >= k:
                return list(list(zip(*ret))[0])[:k]


# print(Solution().topKFrequent(["is", "day", "the", "sunny", "the", "the", "the", "sunny", "is", "is", "is"], k=4))
print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 1))
