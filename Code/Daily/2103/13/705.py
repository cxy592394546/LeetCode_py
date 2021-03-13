class MyHashSet:

    def __init__(self):
        self.table = [[] for _ in range(997)]
        """
        Initialize your data structure here.
        """

    def add(self, key: int) -> None:
        if self.contains(key) is False:
            self.table[key % 997].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.table[key % 997].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.table[key % 997]
        """
        Returns true if this set contains the specified element
        """
