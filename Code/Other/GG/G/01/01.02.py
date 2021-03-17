def func(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    dic = {}
    for i in range(len(s1)):
        if s1[i] not in dic.keys():
            dic[s1[i]] = 1
        else:
            dic[s1[i]] += 1
    for i in range(len(s2)):
        if s2[i] not in dic.keys():
            return False
        else:
            dic[s2[i]] -= 1
            if dic[s2[i]] == 0:
                del dic[s2[i]]
    if len(dic) > 1:
        return False
    return True


if __name__ == '__main__':
    print(func("abc", "ccba"))
