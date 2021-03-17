def func(s: str) -> bool:
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic.keys():
            dic[s[i]] = 1
        else:
            del dic[s[i]]
    return len(dic) <= 1


if __name__ == '__main__':
    print(func('aab'))
