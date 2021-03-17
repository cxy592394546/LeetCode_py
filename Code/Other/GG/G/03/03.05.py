class SortedStack:

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, val: int) -> None:
        if not self.stackA or self.stackA[-1] >= val:
            self.stackA.append(val)
        else:
            while self.stackA and self.stackA[-1] < val:
                self.stackB.append(self.stackA.pop())
            self.stackA.append(val)
            while self.stackB:
                self.stackA.append(self.stackB.pop())

    def pop(self) -> None:
        if self.stackA:
            self.stackA.pop()

    def peek(self) -> int:
        return -1 if not self.stackA else self.stackA[-1]

    def isEmpty(self) -> bool:
        return not self.stackA
