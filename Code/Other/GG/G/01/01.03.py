def func(S: str, length: int) -> str:
    ret = ''
    for i in range(length):
        if len(S) > i and S[i] != ' ':
            ret += S[i]
        else:
            ret += '%20'
    return ret


if __name__ == '__main__':
    print(func("  Mr John Smith", 18))
    print(func("     ", 5))
