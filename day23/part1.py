from queue import LifoQueue

with open("input", "r") as f:
    g = {x + y * 1j: c for y, row in enumerate(f) for x, c in enumerate(row)}

s = LifoQueue()
s.put((1, 0, 1, []))
distances = []
while not s.empty():
    pos, steps, dir, visited = s.get()
    if pos + 1j not in g.keys():
        distances.append(steps)
        continue
    if g[pos] == ">":
        if pos + 1 not in visited:
            s.put((pos + 1, steps + 1, 1, visited + [pos]))
    elif g[pos] == "<":
        if pos - 1 not in visited:
            s.put((pos - 1, steps + 1, -1, visited + [pos]))
    elif g[pos] == "v":
        if pos + 1j not in visited:
            s.put((pos + 1j, steps + 1, 1j, visited + [pos]))
    else:
        for d in 1j / dir, -1j / dir, dir:
            if (pos + d) in g.keys():
                if g[pos + d] != "#":
                    if pos + d not in visited:
                        s.put((pos + d, steps + 1, d, visited + [pos]))
print(max(distances))

