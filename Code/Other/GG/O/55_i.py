import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodes = collections.deque([root])
        level, cur_num, nxt_num = 0, 1, 0
        while nodes:
            while cur_num != 0:
                cur = nodes.popleft()
                if cur.left:
                    nodes.append(cur.left)
                    nxt_num += 1
                if cur.right:
                    nodes.append(cur.right)
                    nxt_num += 1
                cur_num -= 1
            cur_num, nxt_num = nxt_num, cur_num
            level += 1
        return level