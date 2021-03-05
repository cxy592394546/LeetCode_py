from typing import List


def func(num: int) -> List[int]:
    ret = [0]
    gap = 1
    for i in range(1, num + 1):
        ret.append(ret[i - gap] + 1)
        if i == gap:
            gap *= 2
    return ret


if __name__ == '__main__':
    print(func(5))
