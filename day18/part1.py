pos = (0, 0)
corner_points = [pos]
numbp = 0
f = open("input", "r")
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    dir, dist = line.split(" ")[0], int(line.split(" ")[1])
    numbp += dist
    if dir == "R":
        pos = (pos[0], pos[1] + dist)
        corner_points.append(pos)
    elif dir == "L":
        pos = (pos[0], pos[1] - dist)
        corner_points.append(pos)
    elif dir == "D":
        pos = (pos[0] + dist, pos[1])
        corner_points.append(pos)
    elif dir == "U":
        pos = (pos[0] - dist, pos[1])
        corner_points.append(pos)
f.close()

area = 0
for i in range(len(corner_points)):
    area += corner_points[i][0] * corner_points[(i + 1) % len(corner_points)][1]
    area -= corner_points[i][1] * corner_points[(i + 1) % len(corner_points)][0]
area = 0.5 * abs(area)
i = area + 1 - (numbp / 2)
print(numbp + i)

