from typing import List

# TLE
# class Solution:
#     def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
#         sum_matrix = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
#         ret = -float('inf')
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 sum_matrix[i + 1][j + 1] = sum_matrix[i + 1][j] + sum_matrix[i][j + 1] - sum_matrix[i][j] + matrix[i][j]
#         print(sum_matrix)
#         for i in range(1, len(sum_matrix)):
#             for j in range(1, len(sum_matrix[0])):
#                 if sum_matrix[i][j] <= k:
#                     ret = max(ret, sum_matrix[i][j])
#                 for m in range(i, len(sum_matrix)):
#                     for n in range(j, len(sum_matrix[0])):
#                         matrix_val = sum_matrix[m][n] - sum_matrix[m][j - 1] - sum_matrix[i - 1][n] + sum_matrix[i - 1][j - 1]
#                         if matrix_val <= k:
#                             ret = max(ret, matrix_val)
#         return ret


from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])

        for i in range(m):  # 枚举上边界
            total = [0] * n
            for j in range(i, m):  # 枚举下边界
                for c in range(n):
                    total[c] += matrix[j][c]  # 更新每列的元素和

                totalSet = SortedList([0])
                s = 0
                for v in total:
                    s += v
                    lb = totalSet.bisect_left(s - k)
                    if lb != len(totalSet):
                        ans = max(ans, s - totalSet[lb])
                    totalSet.add(s)

        return ans


print(Solution().maxSumSubmatrix([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 3))
print(Solution().maxSumSubmatrix([[2, 2, -1]], 0))
