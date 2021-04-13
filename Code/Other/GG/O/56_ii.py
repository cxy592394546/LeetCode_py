a = [4, 8, 7, 6, 1, 5, 3, 9, 2, 0]
list = [0 for i in range(0, 10)]


def fastSort(l, r, li, ret):
    num = li[l]
    if l >= r:
        return
    l += 1
    while l < r:
        while l < r and li[l] < num:
            l += 1
        while l < r and li[r] > num:
            r -= 1
        if l == r:
            break
        li[l], li[r] = li[r], li[l]
    print(li)


fastSort(0, len(list), list, [])
