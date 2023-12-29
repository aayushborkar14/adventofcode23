f = open("input", "r")
g = {}
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    node, adjn = line.split(": ")[0], line.split(": ")[1].split(" ")
    if node not in g.keys():
        g[node] = set(adjn)
    else:
        g[node] |= set(adjn)
    for v in adjn:
        if v not in g.keys():
            g[v] = {node}
        else:
            g[v] |= {node}
f.close()
all_v = set()
for adjv in g.values():
    all_v |= adjv
s = all_v.copy()
cl = lambda v: len(g[v] - s)
while sum(map(cl, s)) != 3:
    s.remove(max(s, key=cl))
print(len(s) * len(all_v - s))

