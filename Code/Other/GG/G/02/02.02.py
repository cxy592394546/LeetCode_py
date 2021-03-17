class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        node = head
        if head.next is None and k == 1:
            return head.val
        while node.next:
            if k != 1:
                node = node.next
                k -= 1
            else:
                node = node.next
                head = head.next
        return head.val
