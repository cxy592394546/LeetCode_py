op = int(input())
rank = {}
rank_li = []
for i in range(op):
    li = list(map(str, input().split(" ")))
    if li[0] == 'query':
        if len(rank) == 0:
            print('null')
        else:
            ret = ''
            num = 0
            for i in range(len(rank_li)):
                ret += str(rank_li[i][0])
                if i != len(rank_li) - 1:
                    ret += ' '
                num += 1
                if num == 10:
                    break
            print(ret)
    elif li[0] == 'append':
        if li[1] not in rank.keys():
            rank[li[1]] = li[2]
        else:
            rank[li[1]] = str(int(rank[li[1]]) + int(li[2]))
        rank_li = sorted(rank.items(), key=lambda item: item[1], reverse=True)

# 9
# query
# append 1 10
# query
# append 2 20
# query
# append 3 15
# query
# append 1 10
# query
