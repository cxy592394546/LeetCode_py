from typing import List


def func(row: List[int]) -> int:
    res = 0
    for i in range(0, len(row) - 1, 2):
        if row[i] // 2 == row[i + 1] // 2:
            continue
        for j in range(i + 1, len(row)):
            if row[i] // 2 == row[j] // 2:
                row[i + 1], row[j] = row[j], row[i + 1]
        res += 1
    return res


if __name__ == '__main__':
    print(func([0, 2, 1, 3]))
