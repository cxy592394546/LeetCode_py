from typing import List


def func(cardPoints: List[int], k: int):
    val = 0
    mval = 0
    for i in range(0, k):
        val += cardPoints[i]
    print(val)
    for i in range(0, k):
        mval = max(mval, val, val - cardPoints[k - i - 1] + cardPoints[-1 - i])
        val = val - cardPoints[k - i - 1] + cardPoints[-1 - i]
        print(mval, val)
    print(mval)


if __name__ == '__main__':
    func([96, 90, 41, 82, 39, 74, 64, 50, 30], 8)

