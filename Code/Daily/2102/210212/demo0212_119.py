from typing import List


def func(rowIndex: int) -> List:
    rlist = []
    for i in range(rowIndex + 1):
        if i == 0:
            rlist.append(1)
        elif i > rowIndex / 2:
            rlist.append(rlist[rowIndex - i])
        else:
            j = 0
            val = 1
            while j != i:
                val = val * (rowIndex - j) / (j + 1)
                j += 1
            rlist.append(int(val))
    return rlist


if __name__ == '__main__':
    print(func(3))
