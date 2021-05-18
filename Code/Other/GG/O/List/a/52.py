class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        while curA and curB:
            curA, curB = curA.next, curB.next
        if curA:
            while curA:
                headA, curA = headA.next, curA.next
        elif curB:
            while curB:
                headB, curB = headB.next, curB.next
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA
