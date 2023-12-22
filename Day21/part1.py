from collections import deque

with open("input", "r") as f:
    g = [line.strip() for line in f]
NUMSTEPS = 64
start = ()
for i, line in enumerate(g):
    if "S" in line:
        start = (i, line.find("S"), 0)
        break
s = deque()
s.append(start)
ans = 0
visited = []
while len(s):
    x, y, steps = s.pop()
    if (x, y, steps) in visited:
        continue
    visited.append((x, y, steps))
    if steps == NUMSTEPS:
        ans += 1
        continue
    if x + 1 < len(g) and g[x + 1][y] != "#":
        s.append((x + 1, y, steps + 1))
    if x > 0 and g[x - 1][y] != "#":
        s.append((x - 1, y, steps + 1))
    if y + 1 < len(g[x]) and g[x][y + 1] != "#":
        s.append((x, y + 1, steps + 1))
    if y > 0 and g[x][y - 1] != "#":
        s.append((x, y - 1, steps + 1))
print(ans)

