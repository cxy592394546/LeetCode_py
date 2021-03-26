import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []
        ret = []
        queue = collections.deque([tree])
        cur = 1
        while queue:
            head = ListNode(0)
            lNode = head
            while cur != 0:
                tNode = queue.popleft()
                lNode.next = ListNode(tNode.val)
                lNode = lNode.next
                if tNode.left:
                    queue.append(tNode.left)
                if tNode.right:
                    queue.append(tNode.right)
                cur -= 1
            ret.append(head.next)
            cur = len(queue)
        return ret
