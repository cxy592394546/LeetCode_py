#   1.
# a, str1, b = list(map(list, input().split("\"")))
# if len(str1) == 0:
#     print(0)
# else:
#     chars = set()
#     for c in b:
#         if c != ',' and c != '[' and c != ']':
#             chars.add(c)
#     str2 = "#"
#     for c in str1:
#         if c in chars:
#             str2 += "@#"
#         else:
#             str2 += c + "#"
#     ret = 1
#     for i in range(len(str2)):
#         tmp = 1
#         if str2[i] == "#":
#             l, r = i - 1, i + 1
#             if l >= 0 and r < len(str2):
#                 if str2[l] != "@" and str2[l] == str2[r]:
#                     tmp = 2
#                     l -= 2
#                     r += 2
#                     while l >= 0 and r < len(str2):
#                         if str2[l] != "@" and str2[l] == str2[r]:
#                             tmp += 2
#                             l -= 2
#                             r += 2
#                         else:
#                             break
#         elif str2[i] != "#" and str2[i] != "@":
#             l, r = i - 2, i + 2
#             while l >= 0 and r < len(str2):
#                 if str2[l] != "@" and str2[l] == str2[r]:
#                     tmp += 2
#                     l -= 2
#                     r += 2
#                 else:
#                     break
#         ret = max(ret, tmp)
#
# print(ret)
#   2.


#   3.
# class Solution:
#     def minWater(self, height):
#         if len(height) <= 1:
#             return 0
#         min_pool = float("inf")
#         hi_pos, pool = 0, 0
#         for i in range(len(height)):
#             if height[i] < height[hi_pos]:
#                 pool += height[hi_pos] - height[i]
#             elif height[i] >= height[hi_pos]:
#                 if pool != 0:
#                     min_pool = min(min_pool, pool)
#                 pool = 0
#                 hi_pos = i
#         r_pos = len(height) - 1
#         for i in range(len(height) - 1, hi_pos - 1, -1):
#             if height[i] < height[r_pos]:
#                 pool += height[r_pos] - height[i]
#             elif height[i] >= height[r_pos]:
#                 if pool != 0:
#                     min_pool = min(min_pool, pool)
#                 pool = 0
#                 r_pos = i
#         if min_pool == float("inf"):
#             return 0
#         return min_pool
#   4.
class Solution:
    def maxMatch(self, matchPairList):
        jobs = set()
        persons = dict()
        for item in matchPairList:
            if item[1] not in jobs:
                jobs.add(item[1])
        for item in matchPairList:
            if item[0] not in persons:
                persons[item[0]] = {item[1]}
            elif item[0] in persons:
                persons[item[0]].add(item[1])
        dp = [[0] * (len(persons) + 1)] * (len(jobs) + 1)
        jobs = list(jobs)
        for i in range(1, len(dp)):
            print(jobs[i - 1])
            dp[i][0] = jobs[i - 1]
        print(dp)
        print(jobs, persons)
        # persons = dict()
        # person_set = set()
        # # for item in matchPairList:
        # #     if item[1] not in dic:
        # #         dic[item[1]] = {item[0]}
        # #     elif item[1] in dic:
        # #         dic[item[1]].add(item[0])
        # for item in matchPairList:
        #     if item[0] not in persons:
        #         persons[item[0]] = {item[1]}
        #     elif item[0] in persons:
        #         persons[item[0]].add(item[1])
        # persons = sorted(persons.items(), key=lambda item: len(item[1]))
        # for item in persons:
        #     for job in item[1]:
        #         if job not in person_set:
        #             person_set.add(job)
        #             break
        # return len(person_set)


print(Solution().maxMatch([[0, 103], [1, 103], [1, 104], [2, 104], [2, 105], [2, 106], [3, 103]]))
