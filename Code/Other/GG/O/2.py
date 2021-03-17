class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def func(l1: ListNode, l2: ListNode) -> ListNode:
    head = l1
    val1 = val2 = 0
    rate = 1
    while l1 is not None:
        val1 += l1.val * rate
        rate *= 10
        l1 = l1.next
    rate = 1
    l1 = head
    while l2 is not None:
        val2 += l2.val * rate
        rate *= 10
        l2 = l2.next
    val1 += val2
    while val1 > 0:
        node: ListNode(val1 % 10)
        val1 //= 10
        l1.next = node
        l1 = l1.next
    return head


if __name__ == '__main__':
    print(func())
