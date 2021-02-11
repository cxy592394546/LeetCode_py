# def func(s: str) -> str:
#     return s.replace(" ", "%20")


def func(s: str) -> str:
    str1 = ""
    for i in range(len(s)):
        if s[i] == ' ':
            str1 += "%20"
        else:
            str1 += s[i]
    return str1


if __name__ == '__main__':
    print(func("We are happy"))