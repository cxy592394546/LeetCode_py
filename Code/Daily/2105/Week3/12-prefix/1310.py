from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] = arr[i - 1] ^ arr[i]
        arr = [0] + arr
        for i in range(len(queries)):
            queries[i] = arr[queries[i][1] + 1] ^ arr[queries[i][0]]
        return queries