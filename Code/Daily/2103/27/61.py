class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        if count < 2 or k % count == 0:
            return head
        cur = head
        bit = count - k % count
        while bit != 0:
            if bit == 1:
                tmp = cur
                cur = cur.next
                tmp.next = None
            else:
                cur = cur.next
            bit -= 1
        ret = cur
        while cur.next:
            cur = cur.next
        cur.next = head
        return ret
