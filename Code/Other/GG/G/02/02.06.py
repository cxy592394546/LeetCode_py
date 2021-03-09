class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        cur = head
        cut = count // 2
        while cut != 0:
            cur = cur.next
            cut -= 1
        node = cur
        cur = cur.next
        while cur:
            temp = cur.next
            cur.next = node
            node = cur
            cur = temp
        cut = count // 2
        while cut != 0:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
            cut -= 1
        return True
