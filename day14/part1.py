g = []
f = open("input", "r")
while True:
    line = f.readline()
    if not line:
        break
    g.append(line.rstrip())
f.close()
ans = 0
for i in range(len(g[0])):
    m = {-1: 0}
    prev_hash = -1
    for j, s in enumerate(g):
        if s[i] == "O":
            m[prev_hash] += 1
        elif s[i] == "#":
            prev_hash = j
            m[prev_hash] = 0
    for hash, n in m.items():
        a = len(g) - hash - 1
        ans += int(n * (2 * a - (n - 1)) / 2)
print(ans)
