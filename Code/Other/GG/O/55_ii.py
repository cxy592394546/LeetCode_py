class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.subtreeDepth(root) != -1

    def subtreeDepth(self, node):
        if not node:
            return 0
        leftHeight = self.subtreeDepth(node.left)
        rightHeight = self.subtreeDepth(node.right)
        if leftHeight >= 0 and rightHeight >= 0 and abs(leftHeight - rightHeight) < 2:
            return max(leftHeight, rightHeight) + 1
        else:
            return -1


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.right.left = TreeNode(4)
print(Solution().isBalanced(root))
