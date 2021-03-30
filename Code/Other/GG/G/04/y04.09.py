class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        res = []

        def findPath(cur, queue, path):
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            if not queue:
                res.append(path)
                return
            for i, nex in enumerate(queue):
                newq = queue[:i] + queue[i + 1:]
                findPath(nex, newq, path + [nex.val])

        findPath(root, [], [root.val])
        return res
