class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre_node = None
        self.ret = float("inf")

    def minDiffInBST(self, root: TreeNode) -> int:
        self.helper(root)
        return self.ret

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        if self.pre_node:
            self.ret = min(self.ret, node.val - self.pre_node.val)
        self.pre_node = node
        self.helper(node.right)
