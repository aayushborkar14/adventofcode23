g = []
pres = (-1, -1)
f = open("input", "r")
y = 0
while True:
    line = f.readline()
    if not line:
        break
    g.append(line.rstrip())
    for idx, c in enumerate(line.rstrip()):
        if c == "S":
            pres = (y, idx)
    y += 1
f.close()
prev = pres
if (
    g[prev[0]][prev[1] + 1] == "-"
    or g[prev[0]][prev[1] + 1] == "J"
    or g[prev[0]][prev[1] + 1] == "7"
):
    pres = (prev[0], prev[1] + 1)
elif (
    g[prev[0]][prev[1] - 1] == "-"
    or g[prev[0]][prev[1] - 1] == "L"
    or g[prev[0]][prev[1] - 1] == "F"
):
    pres = (prev[0], prev[1] - 1)
elif (
    g[prev[0] + 1][prev[1]] == "|"
    or g[prev[0] + 1][prev[1]] == "L"
    or g[prev[0] + 1][prev[1]] == "J"
):
    pres = (prev[0] + 1, prev[1])
elif (
    g[prev[0] - 1][prev[1]] == "|"
    or g[prev[0] - 1][prev[1]] == "F"
    or g[prev[0] - 1][prev[1]] == "7"
):
    pres = (prev[0] - 1, prev[1])
boundary_points = [prev, pres]
while True:
    nxt = (-1, -1)
    if g[pres[0]][pres[1]] == "L" or g[pres[0]][pres[1]] == "7":
        nxt = (pres[0] + pres[1] - prev[1], pres[1] + pres[0] - prev[0])
    elif g[pres[0]][pres[1]] == "F" or g[pres[0]][pres[1]] == "J":
        nxt = (pres[0] + prev[1] - pres[1], pres[1] + prev[0] - pres[0])
    elif g[pres[0]][pres[1]] == "-" or g[pres[0]][pres[1]] == "|":
        nxt = (2 * pres[0] - prev[0], 2 * pres[1] - prev[1])
    if g[nxt[0]][nxt[1]] == "S":
        break
    boundary_points.append(nxt)
    prev = pres
    pres = nxt
area = 0
for i in range(len(boundary_points)):
    area += boundary_points[i][0] * boundary_points[(i + 1) % len(boundary_points)][1]
    area -= boundary_points[i][1] * boundary_points[(i + 1) % len(boundary_points)][0]
area = 0.5 * abs(area)
i = area + 1 - (len(boundary_points) / 2)
print(i)

