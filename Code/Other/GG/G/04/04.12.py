class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.calculate(root, [], sum)

    def calculate(self, root, vals, sum):
        if not root:
            return 0
        i, cnt = 0, 0
        if root.val == sum:
            cnt += 1
        while i != len(vals):
            if vals[i] + root.val == sum:
                cnt += 1
            vals[i] += root.val
            i += 1
        vals.append(root.val)
        vals_ = vals.copy()
        return self.calculate(root.left, vals, sum) + self.calculate(root.right, vals_, sum) + cnt
