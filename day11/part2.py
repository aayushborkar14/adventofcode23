from bisect import bisect_left

space_multiplier = 1000000

g = []
galactic_coords = []
all_space_y = []
f = open("input", "r")
y = 0
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    g.append(line)
    all_space = True
    for i, c in enumerate(line):
        if c == "#":
            all_space = False
            galactic_coords.append((y, i))
    if all_space:
        all_space_y.append(y)
    y += 1
f.close()
all_space_x = []
for i in range(len(g[0])):
    all_space = True
    for s in g:
        if s[i] == "#":
            all_space = False
            break
    if all_space:
        all_space_x.append(i)
for i, galaxy in enumerate(galactic_coords):
    galactic_coords[i] = (
        galaxy[0] + bisect_left(all_space_y, galaxy[0]) * (space_multiplier - 1),
        galaxy[1] + bisect_left(all_space_x, galaxy[1]) * (space_multiplier - 1),
    )
ans = 0
for idx, a in enumerate(galactic_coords):
    for b in galactic_coords[idx + 1 :]:
        ans += abs(a[0] - b[0]) + abs(a[1] - b[1])
print(ans)

