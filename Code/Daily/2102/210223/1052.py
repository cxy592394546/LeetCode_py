from typing import List


def func(customers: List[int], grumpy: List[int], X: int) -> int:
    customer = 0
    for i in range(len(customers)):
        if grumpy[i] == 0:
            customer += customers[i]
    num = 0
    for i in range(X):
        if grumpy[i] == 1:
            num += customers[i]
    add_c = num
    for i in range(len(customers) - X):
        add_c = max(add_c, num - grumpy[i] * customers[i] + grumpy[i + X] * customers[i + X])
        num = num - grumpy[i] * customers[i] + grumpy[i + X] * customers[i + X]
    customer += add_c
    return customer


if __name__ == '__main__':
    print(func([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
    print(func([4, 10, 10], [1, 1, 0], 2))
