class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        h1, h2 = headA, headB
        count1 = count2 = 0
        while h1:
            h1 = h1.next
            count1 += 1
        while h2:
            h2 = h2.next
            count2 += 1
        h1, h2 = headA, headB
        diff = abs(count1 - count2)
        if count1 > count2:
            while diff != 0:
                diff -= 1
                h1 = h1.next
        else:
            while diff != 0:
                diff -= 1
                h2 = h2.next
        while h1:
            if h1 == h2:
                return h1
            h1 = h1.next
            h2 = h2.next
        return None
