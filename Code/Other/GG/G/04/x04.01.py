from typing import List


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        # 构建邻接表
        link_table = [[] for _ in range(n)]
        for i, j in graph:
            link_table[i].append(j)
        visted = [0]*n # 访问数组
        # BFS
        que = [start]
        while que:
            cur_node = que.pop()
            if target in link_table[cur_node]: return True
            for node in link_table[cur_node]:
                if visted[node]==0:
                    que.insert(0,node)
            visted[cur_node] = 1
        return False






test = Solution()
# print(test.findWhetherExistsPath(3, [[0, 1], [0, 2], [1, 2], [1, 2]], 0, 2))
print(test.findWhetherExistsPath(5, [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], 0,
                                 4))
