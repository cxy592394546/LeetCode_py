li = list(map(int, input().split()))
li23 = []
roads = dict()
for i in range(li[1]):
    a, b, c = list(map(int, input().split()))
    if i == li[2] - 1 or i == li[3] - 1:
        li23 += [(a, b, c)]
    else:
        if c not in roads.keys():
            roads[c] = [(a, b, c)]
        elif c in roads.keys():
            roads[c] += [(a, b, c)]
roads = sorted(roads.items(), key=lambda item: item[0])
roads_li = []
for i in range(len(roads)):
    roads_li += roads[i][1]
points = set()
val, val1, val2 = 0, li23[0][2], li23[1][2]
paths = 0
for item in roads_li:
    flag = False
    if item[0] not in points:
        points.add(item[0])
        flag = True
    if item[1] not in points:
        points.add(item[1])
        flag = True
    if flag:
        paths += 1
        val += item[2]
    if len(points) == li[0]:
        if paths != li[0] - 1:
            val += item[2]
        break
points = {li23[0][0], li23[0][1]}
paths = 1
for item in roads_li:
    flag = False
    if item[0] not in points:
        points.add(item[0])
        flag = True
    if item[1] not in points:
        points.add(item[1])
        flag = True
    if flag:
        paths += 1
        val1 += item[2]
    if len(points) == li[0]:
        if paths != li[0] - 1:
            val += item[2]
        break
val = min(val, val1)
points = {li23[1][0], li23[1][1]}
paths = 1
for item in roads_li:
    flag = False
    if item[0] not in points:
        points.add(item[0])
        flag = True
    if item[1] not in points:
        points.add(item[1])
        flag = True
    if flag:
        paths += 1
        val1 += item[2]
    if len(points) == li[0]:
        if paths != li[0] - 1:
            val += item[2]
        break
val = min(val, val2)
print(val)
