class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        if len(self.stack) == 0:
            return
        cur = self.stack.pop()
        if cur.right:
            while cur.right:
                self.stack.append(cur.right)
                cur.right = cur.right.left
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0
