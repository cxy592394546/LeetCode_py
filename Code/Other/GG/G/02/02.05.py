class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rate = 1
        val = 0
        node = l1
        head = node
        while l1:
            val += l1.val * rate
            rate *= 10
            l1 = l1.next
        rate = 1
        while l2:
            val += l2.val * rate
            rate *= 10
            l2 = l2.next
        node.val = val % 10
        while val >= 10:
            val //= 10
            node.next = ListNode(val % 10)
            node = node.next
        return head
