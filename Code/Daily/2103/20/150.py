from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tmp = []
        for item in tokens:
            if item == "+":
                tmp.append(tmp.pop() + tmp.pop())
            elif item == "-":
                a = tmp.pop()
                tmp.append(tmp.pop() - a)
            elif item == "*":
                tmp.append(tmp.pop() * tmp.pop())
            elif item == "/":
                a = tmp.pop()
                tmp.append(int(tmp.pop() / a))
            else:
                tmp.append(int(item))
            print(tmp)
        return int(tmp[0])


test = Solution()
print(test.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
