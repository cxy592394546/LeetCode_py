class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) < 2 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def depth(self, node) -> int:
        if not node:
            return 0
        else:
            return max(self.depth(node.left), self.depth(node.right)) + 1
