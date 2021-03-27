import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        li = collections.deque([[root, -float("inf"), float("inf")]])
        while li:
            cur = li.popleft()
            if cur[0].left:
                if cur[1] < cur[0].left.val < cur[0].val:
                    li.append([cur[0].left, cur[1], cur[0].val])
                else:
                    return False
            if cur[0].right:
                if cur[0].val < cur[0].right.val < cur[2]:
                    li.append([cur[0].right, cur[0].val, cur[2]])
                else:
                    return False
        return True
