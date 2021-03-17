class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # if preorder == '#':
        #     return True
        # if len(preorder) < 3 or preorder[-1] != '#' or preorder[-3] != '#':
        #     return False
        # treeNode = []
        # num = 0
        # for i in range(len(preorder)):
        #     if preorder[i] == ',':
        #         pass
        #     elif preorder[i] == '#':
        #         treeNode.append('#')
        #     elif preorder[i].isdigit():
        #         num = num * 10 + int(preorder[i])
        #         if i + 1 == len(preorder):
        #             return False
        #         elif preorder[i + 1].isdigit() is False:
        #             treeNode.append(num)
        #             num = 0
        # stack = [2]
        # for i in range(1, len(treeNode)):
        #     if len(stack) == 0:
        #         return False
        #     if treeNode[i] != '#':
        #         if stack[-1] == 1:
        #             stack.pop()
        #         else:
        #             stack[-1] -= 1
        #         stack.append(2)
        #     else:
        #         if stack[-1] == 1:
        #             stack.pop()
        #         else:
        #             stack[-1] -= 1
        # if len(stack) != 0:
        #     return False
        # return True
        if preorder == '#':
            return True
        if len(preorder) < 3 or preorder[-1] != '#' or preorder[-3] != '#':
            return False
        numFlag = 0
        stack = []
        for i in range(len(preorder)):
            if preorder[i] == ',':
                pass
            elif preorder[i] == '#':
                if len(stack) == 0:
                    return False
                if stack[-1] == 1:
                    stack.pop()
                else:
                    stack[-1] -= 1
            elif preorder[i].isdigit():
                numFlag += 1
                if i + 1 == len(preorder):
                    return False
                elif preorder[i + 1].isdigit() is False:
                    numFlag = 0
                    if len(stack) == 0 and i == numFlag:
                        stack.append(2)
                    else:
                        if len(stack) == 0:
                            return False
                        if stack[-1] == 1:
                            stack.pop()
                        else:
                            stack[-1] -= 1
                        stack.append(2)
        if len(stack) != 0:
            return False
        return True


test = Solution()
print(test.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
print(test.isValidSerialization("#,#,#"))
print(test.isValidSerialization("9,3,4,#,#,1,#,#,#,2,#,6,#,#"))
