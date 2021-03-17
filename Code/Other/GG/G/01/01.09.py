def func(s1: str, s2: str) -> bool:  # 旋转字符串拼接！！！
    if len(s1) != len(s2):
        return False
    s2 += s2
    if s1 in s2:
        return True
    return False


if __name__ == '__main__':
    print(func("waterbottle", "erbottlewat"))
