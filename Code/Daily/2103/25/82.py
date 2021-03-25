class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        fNode = ListNode(0, head)
        head = fNode
        while head:
            if head.next and head.next.next:
                if head.next.val == head.next.next.val:
                    while head.next and head.next.next and head.next.val == head.next.next.val:
                        head.next = head.next.next
                    head.next = head.next.next
                else:
                    head = head.next
            else:
                head = head.next
        return fNode.next
