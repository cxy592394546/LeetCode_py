class StackOfPlates:

    def __init__(self, cap: int):
        self.stacks = []
        self.cap = cap

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        if self.stacks and len(self.stacks[-1]) < self.cap:
            self.stacks[-1].append(val)
            return
        self.stacks.append([val])

    def pop(self) -> int:
        if self.cap == 0:
            return -1
        if len(self.stacks) == 0:
            return -1
        ret = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            del self.stacks[-1]
        return ret

    def popAt(self, index: int) -> int:
        if self.cap == 0:
            return -1
        if index >= len(self.stacks) or len(self.stacks[index]) == 0:
            return -1
        ret = self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            del self.stacks[index]
        return ret
