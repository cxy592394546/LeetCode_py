class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        set0 = set()
        while head is not None:
            if head in set0:
                return head
            set0.add(head)
            head = head.next
        return None
