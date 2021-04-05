from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pos, pos1, pos2 = len(nums1) - 1, m - 1, n - 1
        while pos1 > -1 and pos2 > -1:
            if nums1[pos1] > nums2[pos2]:
                nums1[pos] = nums1[pos1]
                pos1 -= 1
            else:
                nums1[pos] = nums2[pos2]
                pos2 -= 1
            pos -= 1
        while pos2 > -1:
            nums1[pos] = nums2[pos2]
            pos -= 1
            pos2 -= 1
        """
        Do not return anything, modify nums1 in-place instead.
        """


test = Solution()
print(test.merge([3, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
