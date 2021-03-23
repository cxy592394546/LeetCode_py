class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.index = 0
        self.ret = []
        self.makeList(nestedList)

    def next(self) -> int:
        return self.ret[self.index - 1]

    def hasNext(self) -> bool:
        if self.index != len(self.ret):
            self.index += 1
            return True
        return False

    def makeList(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.ret.append(item.getInteger())
            else:
                self.makeList(item.getList())
