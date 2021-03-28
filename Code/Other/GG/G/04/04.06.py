class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        node = None
        while p.val != root.val:
            if p.val < root.val:
                node = root
                root = root.left
            elif p.val > root.val:
                root = root.right
        if not root.right:
            return node
        else:
            root = root.right
            while root.left:
                root = root.left
            return root
        return
