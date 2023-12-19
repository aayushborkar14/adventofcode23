from heapq import heappop, heappush

g = []
f = open("input", "r")
while True:
    line = f.readline()
    if not line:
        break
    g.append(line.rstrip())
f.close()
G = {r + i * 1j: int(c) for i, row in enumerate(g) for r, c in enumerate(row)}

end = (len(g[0]) - 1) + (len(g) - 1) * 1j


def dj(min, max):
    # cost (also priority), entry order (tie-breaker), position, direction taken to arrive
    q = [(0, 0, 0, 1), (0, 1, 0, 1j)]
    x = 1
    visited = set()
    while q:
        cost, _, pos, dir = heappop(q)
        if pos == end:
            return cost
        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))
        for d in 1j / dir, -1j / dir:
            for i in range(min, max + 1):
                if pos + d * i in G:
                    c = sum(G[pos + d * j] for j in range(1, i + 1))
                    heappush(q, (cost + c, (x := x + 1), pos + d * i, d))


print(dj(1, 3))

