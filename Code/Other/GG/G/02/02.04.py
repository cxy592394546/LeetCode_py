class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = head
        while cur.next:
            if cur.val >= x:
                pre = cur
                break
            cur = cur.next
        pre = cur
        while pre:
            if pre.val < x:
                temp = pre.val
                pre.val = cur.val
                cur.val = temp
                cur = cur.next
            pre = pre.next
        return head
