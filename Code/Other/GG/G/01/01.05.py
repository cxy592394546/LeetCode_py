def func(first: str, second: str) -> bool:
    if len(first) <= 1 and len(second) <= 1:
        return True
    if abs(len(first) - len(second)) > 1:
        return False
    flag = True
    i = j = 0
    while i != len(first):
        if j + 1 > len(second):
            break
        if first[i] == second[j]:
            pass
        else:
            if flag is False:
                return False
            else:
                if i + 1 == len(first) and j + 1 == len(second):
                    return True
                elif i + 1 == len(first) or j + 1 == len(second):
                    return False
                if first[i + 1] == second[j + 1]:
                    pass
                elif first[i] == second[j + 1]:
                    j += 1
                elif first[i + 1] == second[j]:
                    j -= 1
                else:
                    return False
                flag = False
        i += 1
        j += 1
        print(i, j, flag)
    return (i == len(first) and j == len(second)) or flag


if __name__ == '__main__':
    print(func("islander", "slander"))
