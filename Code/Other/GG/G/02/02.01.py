class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        node = head
        dic = {node.val}
        while node.next:
            if node.next.val not in dic:
                dic.add(node.next.val)
                node = node.next
            else:
                node.next = node.next.next
        return head
