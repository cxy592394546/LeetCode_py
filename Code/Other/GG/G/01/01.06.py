def func(S: str) -> str:
    if len(S) == 0:
        return ''
    i = 0
    counter = 1
    ret = ''
    while i != len(S):
        if i + 1 != len(S) and S[i + 1] == S[i]:
            counter += 1
        else:
            ret += S[i] + str(counter)
            counter = 1
        i += 1
    if len(ret) >= len(S):
        ret = S
    return ret


if __name__ == '__main__':
    print(func('aabcccccaaa'))
