class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.vals = []
        self.helper(root)
        root = TreeNode()
        node = root
        for num in self.vals:
            node.right = TreeNode(num)
            node = node.right
        return root.right

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.vals.append(node.val)
        self.helper(node.right)
        return
