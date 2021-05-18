import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        nodes = collections.deque([root])
        vals = set()
        cur_level, nxt_level = 1, 0
        while nodes:
            while cur_level != 0:
                cur = nodes.popleft()
                cur_level -= 1
                if cur.left and cur.right and (
                        (cur.left.val == x and cur.right.val == y) or (cur.left.val == y and cur.right.val == x)):
                    return False
                if cur.left:
                    vals.add(cur.left.val)
                    nodes.append(cur.left)
                    nxt_level += 1
                if cur.right:
                    vals.add(cur.right.val)
                    nodes.append(cur.right)
                    nxt_level += 1
            if x in vals and y in vals:
                return True
            vals.clear()
            cur_level, nxt_level = nxt_level, cur_level
        return False
