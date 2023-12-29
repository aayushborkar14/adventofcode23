def intersect(a, b):
    if a[0] <= b[0] and b[0] <= a[1] and a[1] <= b[1]:
        return (b[0], a[1])
    if a[0] >= b[0] and a[1] <= b[1]:
        return (a[0], a[1])
    if b[0] >= a[0] and b[1] <= a[1]:
        return (b[0], b[1])
    if b[0] <= a[0] and a[0] <= b[1] and b[1] <= a[1]:
        return (a[0], b[1])
    return (-1, -1)


def intersection(block1, block2):
    intersect1 = ()
    intersect2 = ()
    null_sect = False
    if block1[0][0] == block1[1][0]:
        if block2[0][0] == block2[1][0]:
            if block1[0][0] == block2[0][0]:
                isect = intersect(
                    (block1[0][1], block1[1][1]), (block2[0][1], block2[1][1])
                )
                if isect[0] == -1:
                    null_sect = True
                else:
                    intersect1 = (block1[0][0], isect[0])
                    intersect2 = (block1[0][0], isect[1])
                    return (intersect1, intersect2)
            else:
                null_sect = True
        if block2[0][1] == block2[1][1]:
            if (block1[0][1] <= block2[0][1] and block2[0][1] <= block1[1][1]) and (
                block2[0][0] <= block1[0][0] and block1[0][0] <= block2[1][0]
            ):
                intersect1 = (block1[0][0], block2[0][1])
                return (intersect1, intersect1)
            else:
                null_sect = True
    if block1[0][1] == block1[1][1]:
        if block2[0][1] == block2[1][1]:
            if block2[0][1] == block1[0][1]:
                isect = intersect(
                    (block2[0][0], block2[1][0]), (block1[0][0], block1[1][0])
                )
                if isect[0] == -1:
                    null_sect = True
                else:
                    intersect1 = (isect[0], block1[0][1])
                    intersect2 = (isect[1], block1[0][1])
                    return (intersect1, intersect2)
            else:
                null_sect = True
        if block2[0][0] == block2[1][0]:
            if (block2[0][1] <= block1[0][1] and block1[0][1] <= block2[1][1]) and (
                block1[0][0] <= block2[0][0] and block2[0][0] <= block1[1][0]
            ):
                intersect1 = (block2[0][0], block1[0][1])
                return (intersect1, intersect1)
            else:
                null_sect = True
    if null_sect:
        return -1


zlist = {k: [] for k in range(1, 337)}
f = open("input", "r")
coord_no = -1
while True:
    line = f.readline()
    if not line:
        break
    coord_no += 1
    line = line.rstrip()
    coord1, coord2 = tuple(tuple(map(int, x.split(","))) for x in line.split("~"))
    if coord1[2] == coord2[2]:
        if coord1[0] == coord2[0]:
            if coord1[1] <= coord2[1]:
                zlist[coord1[2]].append((coord1, coord2, coord_no))
            else:
                zlist[coord1[2]].append((coord2, coord1, coord_no))
        else:
            if coord1[0] <= coord2[0]:
                zlist[coord1[2]].append((coord1, coord2, coord_no))
            else:
                zlist[coord1[2]].append((coord2, coord1, coord_no))
    else:
        if coord2[2] >= coord1[2]:
            for i in range(coord1[2], coord2[2] + 1):
                zlist[i].append((coord1, coord2, coord_no))
        else:
            for i in range(coord2[2], coord1[2] + 1):
                zlist[i].append((coord2, coord1, coord_no))
f.close()
handled = set()
for z in range(2, 337):
    for block in list(zlist[z]):
        if block[2] in handled:
            continue
        handled.add(block[2])
        clear_depth = 0
        while True:
            if z - clear_depth - 1 < 1:
                break
            clearbelow = True
            coord1, coord2 = block[0], block[1]
            if coord1[2] == coord2[2] and coord1[2] != z:
                continue
            for blockd in zlist[z - clear_depth - 1]:
                coordd1, coordd2 = blockd[0], blockd[1]
                if intersection(block, blockd) != -1:
                    clearbelow = False
                    break
            if clearbelow:
                clear_depth += 1
            else:
                break
        if clear_depth:
            blockm = (
                (block[0][0], block[0][1], block[0][2] - clear_depth),
                (block[1][0], block[1][1], block[1][2] - clear_depth),
                block[2],
            )
            if block[0][2] == block[1][2]:
                zlist[z].remove(block)
                zlist[z - clear_depth].append(blockm)
            else:
                for i in range(block[0][2], block[1][2] + 1):
                    zlist[i].remove(block)
                    zlist[i - clear_depth].append(blockm)
supporting = [[] for _ in range(coord_no + 1)]
supportedby = [[] for _ in range(coord_no + 1)]
for z in range(1, 336):
    if not zlist[z + 1]:
        break
    for block in zlist[z]:
        if z != block[1][2]:
            continue
        for blockd in zlist[z + 1]:
            if intersection(block, blockd) != -1:
                supporting[block[2]].append(blockd[2])
                supportedby[blockd[2]].append(block[2])
ans = 0
for blockno in range(coord_no + 1):
    canberm = True
    for blockdno in supporting[blockno]:
        if len(supportedby[blockdno]) <= 1:
            canberm = False
            break
    if canberm:
        ans += 1
print(ans)

