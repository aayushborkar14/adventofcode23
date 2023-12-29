from queue import LifoQueue
from collections import defaultdict

pos_dirs = (1, -1, 1j, -1j)
m = {"#": "#", ".": ".", ">": ".", "<": ".", "v": ".", "^": "."}
with open("input", "r") as f:
    g = {
        x + y * 1j: m[c]
        for y, row in enumerate(f)
        for x, c in enumerate(row.rstrip())
        if c != "#"
    }
neigh = {
    node: [node + dir for dir in pos_dirs if node + dir in g.keys()]
    for node in g.keys()
}
end = next(reversed(g))
juncs = set()
for node in g.keys():
    if len(neigh[node]) != 2:
        juncs.add(node)
el = {}
adj = defaultdict(set)
for junc in juncs:
    for next in neigh[junc]:
        pres = next
        prev = junc
        val = 0
        while pres not in juncs:
            val += 1
            for dir in pos_dirs:
                if pres + dir in g.keys() and prev != pres + dir:
                    prev = pres
                    pres += dir
                    break
        if ((pres, junc) not in el) and ((junc, pres) not in el):
            el[(junc, pres)] = val
            adj[pres].add(junc)
            adj[junc].add(pres)
s = LifoQueue()
s.put((1, 0, []))
distances = []
while not s.empty():
    u, steps, visited = s.get()
    if u == end:
        distances.append(steps)
        continue
    for v in adj[u]:
        if v not in visited:
            dist = 0
            if (v, u) in el.keys():
                dist = el[(v, u)]
            else:
                dist = el[(u, v)]
            s.put((v, steps + dist + 1, visited + [u]))
print(max(distances))

