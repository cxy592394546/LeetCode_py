class MyQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        self.stackA.append(x)
        """
        Push element x to the back of queue.
        """

    def pop(self) -> int:
        if not self.stackB:
            if not self.stackA:
                return
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB.pop()
        """
        Removes the element from in front of queue and returns that element.
        """

    def peek(self) -> int:
        if not self.stackB:
            if not self.stackA:
                return
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB[-1]
        """
        Get the front element.
        """

    def empty(self) -> bool:
        if self.stackA or self.stackB:
            return False
        return True
        """
        Returns whether the queue is empty.
        """
