class MinStack:

    def __init__(self):
        self.stack = []
        """
        initialize your data structure here.
        """

    def push(self, x: int) -> None:
        if self.stack and x >= self.stack[-1][1]:
            self.stack.append([x, self.stack[-1][1]])
        else:
            self.stack.append([x, x])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]
