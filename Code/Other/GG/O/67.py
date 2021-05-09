class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip()
        flag = False
        if str == '':
            return 0
        if str[0] == '-':
            str = str[1:]
            flag = True
        elif str[0] == '+':
            str = str[1:]
        ret = 0
        for i in range(len(str)):
            if '9' >= str[i] >= '0':
                ret = ret * 10 + ord(str[i]) - ord('0')
                if not flag and ret >= 2147483647:
                    return 2147483647
                elif flag and ret >= 2147483648:
                    return -2147483648
            else:
                break
        return ret if not flag else -ret