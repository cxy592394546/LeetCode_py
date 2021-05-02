class MaxQueue:

    def __init__(self):
        self.queue = collections.deque()
        self.m_val = collections.deque()

    def max_value(self) -> int:
        if not self.queue:
            return -1
        return self.m_val[0]

    def push_back(self, value: int) -> None:
        if not self.queue:
            self.queue.append(value)
            self.m_val.append(value)
        else:
            self.queue.append(value)
            while self.m_val and value > self.m_val[-1]:
                if self.m_val[-1] >= value:
                    break
                self.m_val.pop()
            self.m_val.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        tmp = self.queue.popleft()
        if self.m_val[0] == tmp:
            self.m_val.popleft()
        return tmp