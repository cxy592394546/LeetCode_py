class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


head = Node(0)
node = head
tail = Node(0)
for i in range(1, 5):
    node.next = Node(i)
    node = node.next
    if i == 4:
        tail = node
cur = head
while cur:
    print(cur.val)
    cur = cur.next
cur, rev = head, None
while cur:
    rev, rev.next, cur = cur, rev, cur.next
cur = tail
while cur:
    print(cur.val)
    cur = cur.next
