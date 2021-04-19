op = int(input())
li = []
trains, rank = {}, []
for i in range(op):
    a, b, c = list(map(str, input().split()))
    if a == '1':
        b = int(b)
        if c not in trains.keys():
            trains[c] = [b]
            rank.append(c)
        else:
            trains[c].append(b)
    if a == '2':
        tmp1, tmp2 = -1, -1
        for j in range(len(rank)):
            if rank[j] == b:
                tmp1 = j
            if rank[j] == c:
                tmp2 = j
        rank[tmp1], rank[tmp2] = rank[tmp2], rank[tmp1]
ret = ''
print(rank, trains)
for i in range(len(rank)):
    for val in trains[rank[i]]:
        ret += str(val)
        if i != len(rank) - 1 or j != len(trains) - 1:
            ret += ' '
print(ret)
