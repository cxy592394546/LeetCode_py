class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        vals = []
        self.helper(vals, root.right)
        if len(vals) >= k:
            return vals[k - 1]
        elif len(vals) == k - 1:
            return root.val
        k = k - len(vals) - 2
        vals = []
        self.helper(vals, root.left)
        return vals[k]
