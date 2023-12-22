from heapq import heappush, heappop

with open("input", "r") as f:
    g = [line.strip() for line in f]
NUMSTEPS = 64
start = ()
for i, line in enumerate(g):
    if "S" in line:
        start = (0, (i, line.find("S")))
        break
pq = []
heappush(pq, start)
visited = set()
even = 0
odd = 0
eveng65 = 0
oddg65 = 0

while len(pq):
    steps, (x, y) = heappop(pq)
    if (x, y) in visited:
        continue
    visited.add((x, y))
    if steps % 2 == 0:
        even += 1
        if steps > 65:
            eveng65 += 1
    else:
        odd += 1
        if steps > 65:
            oddg65 += 1
    if x + 1 < len(g) and g[x + 1][y] != "#":
        heappush(pq, (steps + 1, (x + 1, y)))
    if x > 0 and g[x - 1][y] != "#":
        heappush(pq, (steps + 1, (x - 1, y)))
    if y + 1 < len(g[x]) and g[x][y + 1] != "#":
        heappush(pq, (steps + 1, (x, y + 1)))
    if y > 0 and g[x][y - 1] != "#":
        heappush(pq, (steps + 1, (x, y - 1)))
n = 202300
ans = ((n + 1) ** 2) * odd + (n**2) * even - (n + 1) * oddg65 + n * eveng65
print(ans)

