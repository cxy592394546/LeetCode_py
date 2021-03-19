class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        ret = ListNode(0, head)
        pre = ret
        count = 1
        while count != left:
            pre = pre.next
            count += 1
        cur = pre.next
        while count != right:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
            count += 1
        return ret.next
