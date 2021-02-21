def func(s1: str, s2: str) -> bool:
    dict1 = {}
    if len(s1) > len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] in dict1:
            dict1[s1[i]] += 1
        else:
            dict1[s1[i]] = 1
    left = 0
    while left < len(s2) - len(s1) + 1:
        dict2 = dict1.copy()  # 这里应该使用字典的浅复制而不是直接复制字典
        for i in range(len(s1)):
            if s2[left + i] not in dict2:
                break
            else:
                dict2[s2[left + i]] -= 1
                if dict2[s2[left + i]] == -1:
                    break
                if i == len(s1) - 1:
                    return True
        left += 1
    return False


if __name__ == '__main__':
    print(func("asfzg", "asfaagadgas"))
