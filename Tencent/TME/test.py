# a, b = list(map(int, input().split()))
# li = ["a" for _ in range(a)]
# for i in range(a):
#     li[i] = list(input())
#
#
# def dfs(c, i, j):
#     if li[i][j] == c:
#         li[i][j] = '@'
#         if a - 1 > i > 0 and b - 1 > j > 0:
#             dfs(c, i - 1, j)
#             dfs(c, i, j - 1)
#             dfs(c, i + 1, j)
#             dfs(c, i, j + 1)
#         elif i == 0 and b - 1 > j > 0:
#             dfs(c, i, j - 1)
#             dfs(c, i, j + 1)
#             dfs(c, i + 1, j)
#         elif i == a - 1 and b - 1 > j > 0:
#             dfs(c, i, j - 1)
#             dfs(c, i, j + 1)
#             dfs(c, i - 1, j)
#         elif a - 1 > i > 0 and j == 0:
#             dfs(c, i - 1, j)
#             dfs(c, i, j + 1)
#             dfs(c, i + 1, j)
#         elif a - 1 > i > 0 and j == b - 1:
#             dfs(c, i, j - 1)
#             dfs(c, i - 1, j)
#             dfs(c, i + 1, j)
#         elif i == 0 and j == b - 1:
#             dfs(c, i + 1, j)
#             dfs(c, i, j - 1)
#         elif i == a - 1 and j == b - 1:
#             dfs(c, i - 1, j)
#             dfs(c, i, j - 1)
#         elif i == 0 and j == 0:
#             dfs(c, i + 1, j)
#             dfs(c, i, j + 1)
#         elif i == a - 1 and j == 0:
#             dfs(c, i - 1, j)
#             dfs(c, i, j + 1)
#
#
# count = 0
# for i in range(a):
#     for j in range(b):
#         if li[i][j] == '1' or li[i][j] == '2' or li[i][j] == '3':
#             count += 1
#             dfs(li[i][j], i, j)
# print(li)
# print(count)


n = int(input())
for i in range(n):
    pos_num = int(input())
    dic = dict()
    for j in range(pos_num - 1):
        a, b = list(map(int, input().split()))
        if a not in dic.keys():
            dic[a] = [b]
        else:
            dic[a] += [b]
        if b not in dic.keys():
            dic[b] = [a]
        else:
            dic[b] += [a]
    # dic = sorted(dic.items(), key=lambda dic: len(dic[1]), reverse=True)
    m_len = 0
    m_val = []
    for k, v in dic.items():
        if len(v) == m_len:
            m_val += [k]
        elif len(v) > m_len:
            m_len = len(v)
            m_val = [k]
    if len(m_val) == 1:
        print(str(m_val[0]) + ' ' + str(dic[m_val[0]][0]))
        print(str(dic[m_val[0]][0]) + ' ' + str(m_val[0]))
    elif len(m_val) != 1:
        if dic[m_val[1]][0] == m_val[0]:
            print(str(m_val[1]) + ' ' + str(dic[m_val[1]][1]))
            print(str(dic[m_val[1]][1]) + ' ' + str(m_val[0]))
        else:
            print(str(m_val[1]) + ' ' + str(dic[m_val[1]][0]))
            print(str(dic[m_val[1]][0]) + ' ' + str(m_val[0]))
    # if len(dic[0][1]) != len(dic[1][1]):
    #     print(str(dic[0][0]) + ' ' + str(dic[0][1][0]))
    #     print(str(dic[0][1][0]) + ' ' + str(dic[0][0]))
    # elif len(dic[0][1]) == len(dic[1][1]):
    #     if dic[1][1][0] == dic[0][0]:
    #         print(str(dic[1][0]) + ' ' + str(dic[1][1][1]))
    #         print(str(dic[1][1][1]) + ' ' + str(dic[0][0]))
