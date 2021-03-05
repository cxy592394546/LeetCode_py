def func(astr: str) -> bool:  # 位运算
    flag = 0
    for i in range(len(astr)):
        num = ord(astr[i]) - ord('a')
        if flag & (1 << num) != 0:
            return False
        else:
            flag |= (1 << num)
    return True


if __name__ == '__main__':
    print("leetcode")
