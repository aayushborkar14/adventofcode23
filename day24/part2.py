from sympy import symbols, Eq, solve

x, y, z, cx, cy, cz = symbols("x y z cx cy cz")

# pv: list = [((x,y,z), (vx,vy,vz))]
pv = [
    tuple(map(tuple, [map(int, x.split(",")) for x in line.split("@")]))
    for line in open("input", "r")
]
equations = [
    Eq((x - xd) * (cy - cyd), (y - yd) * (cx - cxd))
    for ((xd, yd, zd), (cxd, cyd, czd)) in pv
]
equations += [
    Eq((x - xd) * (cz - czd), (z - zd) * (cx - cxd))
    for ((xd, yd, zd), (cxd, cyd, czd)) in pv
]
solution = solve(equations, (x, y, z, cx, cy, cz))
print(solution[0][0] + solution[0][1] + solution[0][2])

