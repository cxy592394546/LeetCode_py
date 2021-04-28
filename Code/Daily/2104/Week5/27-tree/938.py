import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        nodes = collections.deque([root])
        ret = 0
        while nodes:
            cur = nodes.popleft()
            if cur.val < low:
                if cur.right:
                    nodes.append(cur.right)
            elif cur.val > high:
                if cur.left:
                    nodes.append(cur.left)
            else:
                ret += cur.val
                if cur.left:
                    nodes.append(cur.left)
                if cur.right:
                    nodes.append(cur.right)
        return ret
