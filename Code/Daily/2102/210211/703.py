import heapq
from typing import List


def __init__(self, k: int, nums: List[int]):  # 最小堆
    self.pool = nums
    heapq.heapify(self.pool)
    self.k = k
    while len(self.pool) > k:
        heapq.heappop(self.pool)


def add(self, val: int) -> int:
    if len(self.pool) < self.k:
        heapq.heappush(self.pool, val)
    elif val > self.pool[0]:
        heapq.heapreplace(self.pool, val)
    return self.pool[0]