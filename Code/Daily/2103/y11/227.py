class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 1:
            return ord(s) - ord('0')
        s += '#'
        op = '+'
        num = i = 0
        stack = []
        while i != len(s):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            elif s[i] == ' ':
                pass
            else:  # 根据前一个符号进行计算并在计算后将前一符号更新为当前符号
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(num * stack.pop())
                elif op == '/':
                    if stack[-1] < 0 and (stack[-1] % num) != 0:
                        stack.append(stack.pop() // num + 1)
                    else:
                        stack.append(stack.pop() // num)
                op = s[i]
                num = 0
            i += 1

        print(stack, sum(stack))
        return sum(stack)


test = Solution()
print(test.calculate('14 -3 / 2'))
print(test.calculate('999*111-999/111'))
