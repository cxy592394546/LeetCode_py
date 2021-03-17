class TripleInOne:
    def __init__(self, stackSize: int):
        self.stackSize = stackSize
        self.stack = [[], [], []]

    def push(self, stackNum: int, value: int) -> None:
        if len(self.stack[stackNum]) < self.stackSize:
            self.stack[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if len(self.stack[stackNum]) != 0:
            return self.stack[stackNum].pop()
        else:
            return -1

    def peek(self, stackNum: int) -> int:
        if len(self.stack[stackNum]) != 0:
            return self.stack[stackNum][-1]
        else:
            return -1

    def isEmpty(self, stackNum: int) -> bool:
        return len(self.stack[stackNum]) == 0
