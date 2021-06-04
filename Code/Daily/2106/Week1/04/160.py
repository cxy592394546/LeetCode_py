class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        while curA and curB:
            curA = curA.next
            curB = curB.next
        while curA:
            headA = headA.next
            curA = curA.next
        while curB:
            headB = headB.next
            curB = curB.next
        while headA:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
