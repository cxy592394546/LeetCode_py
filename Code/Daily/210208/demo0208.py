from typing import List


def func(arr: List[int]) -> int:
    m_val = 2
    val = 2
    flag = 0
    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i + 1]:
            flag += 1
    if flag == len(arr) - 1:
        return 1
    if len(arr) == 1 or len(arr) == 2:
        return len(arr)
    for i in range(1, len(arr) - 1):
        if op(arr[i], arr[i + 1]) == '>' and op(arr[i - 1], arr[i]) == '<':
            val += 1
        elif op(arr[i], arr[i + 1]) == '<' and op(arr[i - 1], arr[i]) == '>':
            val += 1
        else:
            m_val = max(m_val, val)
            val = 2
    m_val = max(m_val, val)
    return m_val


def op(a: int, b: int) -> str:
    if a > b:
        flag = '>'
    elif a < b:
        flag = '<'
    else:
        flag = '='
    return flag


if __name__ == '__main__':
    print(func([8, 8, 8, 8]))
