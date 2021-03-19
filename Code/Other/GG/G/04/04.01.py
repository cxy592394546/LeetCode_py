from typing import List


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        if len(graph) == 0:
            return False
        i = len(graph) - 1
        graph = sorted(graph, key=lambda k: (k[0], k[1]))
        while i != 0:
            if graph[i][0] == graph[i - 1][0] and graph[i][1] == graph[i - 1][1]:
                graph.pop(i)
            i -= 1
        print(graph)


test = Solution()
# print(test.findWhetherExistsPath(3, [[0, 1], [0, 2], [1, 2], [1, 2]], 0, 2))
print(test.findWhetherExistsPath(5, [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], 0,
                                 4))
