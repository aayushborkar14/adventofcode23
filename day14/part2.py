def load_calc(gr):
    load = 0
    for i in range(len(gr)):
        for j in range(len(gr[i])):
            if gr[i][j] == "O":
                load += len(gr) - i
    return load


g = []
f = open("input", "r")
while True:
    line = f.readline()
    if not line:
        break
    g.append(line.rstrip())
f.close()
dp1 = []
dp2 = []
r = 0
s = 0
while True:
    # North tilt
    grot = []
    for i in range(len(g[0])):
        s = "".join([s[i] for s in g])
        while s.find(".O") != -1:
            s = s.replace(".O", "O.")
        grot.append(s)
    for i in range(len(g)):
        g[i] = "".join([s[i] for s in grot])
    # West tilt
    for i in range(len(g)):
        while g[i].find(".O") != -1:
            g[i] = g[i].replace(".O", "O.")
    # South tilt
    grot = []
    for i in range(len(g[0])):
        s = "".join([s[i] for s in g])
        while s.find("O.") != -1:
            s = s.replace("O.", ".O")
        grot.append(s)
    for i in range(len(g)):
        g[i] = "".join([s[i] for s in grot])
    # East tilt
    for i in range(len(g)):
        while g[i].find("O.") != -1:
            g[i] = g[i].replace("O.", ".O")
    gstring = "".join(g)
    if gstring in dp1:
        r = dp1.index(gstring)
        s = len(dp1)
        break
    dp1.append(gstring)
    dp2.append(load_calc(g))
x = 1000000000
print(dp2[r + (x - 1 - r) % (s - r)])

