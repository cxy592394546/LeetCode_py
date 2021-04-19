class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


a, b, c = list(map(int, input().split()))
root = Node(c)
for i in range(b):
    l, m, n = list(map(int, input().split()))

    root.left = Node(m)
    root.right = Node(n)
