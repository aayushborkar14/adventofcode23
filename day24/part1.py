# pv: list = [((x,y,z), (vx,vy,vz))]
pv = [
    tuple(map(tuple, [map(int, x.split(",")) for x in line.split("@")]))
    for line in open("input", "r")
]
coord_min = 200000000000000
coord_max = 400000000000000
num_sect = 0
for i, pv1 in enumerate(pv):
    x1, y1 = pv1[0][0], pv1[0][1]
    vx1, vy1 = pv1[1][0], pv1[1][1]
    for pv2 in pv[i + 1 :]:
        try:
            x2, y2 = pv2[0][0], pv2[0][1]
            vx2, vy2 = pv2[1][0], pv2[1][1]
            y = (vx1 * y1 / vy1 - vx2 * y2 / vy2 + x2 - x1) / (vx1 / vy1 - vx2 / vy2)
            x = (vy1 * x1 / vx1 - vy2 * x2 / vx2 + y2 - y1) / (vy1 / vx1 - vy2 / vx2)
            if coord_min <= x and x <= coord_max and coord_min <= y and y <= coord_max:
                if (
                    (x - x1) * vx1 >= 0
                    and (y - y1) * vy1 >= 0
                    and (x - x2) * vx2 >= 0
                    and (y - y2) * vy2 >= 0
                ):
                    num_sect += 1
        except:
            # paths are parallel
            pass
print(num_sect)

