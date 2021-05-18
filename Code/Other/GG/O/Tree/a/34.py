import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []
        root.val = [root.val]
        nodes = collections.deque([root])
        cur_level, nxt_level = 1, 0
        ret = []
        while nodes:
            while cur_level != 0:
                cur = nodes.popleft()
                cur_level -= 1
                if cur.left:
                    tmp = cur.left.val
                    cur.left.val = cur.val.copy()
                    cur.left.val.append(tmp)
                    nodes.append(cur.left)
                    nxt_level += 1
                if cur.right:
                    tmp = cur.right.val
                    cur.right.val = cur.val.copy()
                    cur.right.val.append(tmp)
                    nodes.append(cur.right)
                    nxt_level += 1
                if sum(cur.val) == target:
                    if not cur.left and not cur.right:
                        ret.append(cur.val)
            cur_level, nxt_level = nxt_level, cur_level
        return ret
