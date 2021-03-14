class MyHashMap:

    def __init__(self):
        self.table = [[] for _ in range(997)]
        """
        Initialize your data structure here.
        """

    def put(self, key: int, value: int) -> None:
        for item in self.table[key % 997]:
            if item[0] == key:
                item[1] = value
                return
        self.table[key % 997].append([key, value])
        """
        value will always be non-negative.
        """

    def get(self, key: int) -> int:
        for item in self.table[key % 997]:
            if item[0] == key:
                return item[1]
        return -1
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

    def remove(self, key: int) -> None:
        i = 0
        for item in self.table[key % 997]:
            if item[0] == key:
                self.table[key % 997].pop(i)
                return
            i += 1
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
