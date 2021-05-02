from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height = len(wall)
        dic = {}
        counter = 0
        for i in range(len(wall)):
            counter += len(wall[i])
        if counter == len(wall):
            return counter

        for i in range(0, height):
            place = 0
            for j in range(0, len(wall[i]) - 1):
                place += wall[i][j]
                if place in dic:
                    dic[place] += 1
                else:
                    dic[place] = 1

        return height - max(dic.values())


print(Solution().leastBricks([[100000000, 100000000], [100000000, 100000000]]))
print(Solution().leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]))
