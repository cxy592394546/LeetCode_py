class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def preorder(node, li):
            if not node:
                return
            if not node.left and not node.right:
                li += [node.val]
            preorder(node.left, li)
            preorder(node.right, li)

        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        li1, li2 = [], []
        preorder(root1, li1)
        preorder(root2, li2)
        return li1 == li2