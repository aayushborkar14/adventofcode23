import sys

sys.setrecursionlimit(15000)


def mark_visited(i, j, dir):
    if m[i][j] == ".":
        if visited[dir][i][j]:
            return
        visited[dir][i][j] = True
        if dir == "u" and i > 0:
            mark_visited(i - 1, j, dir)
        elif dir == "d" and i + 1 < len(m):
            mark_visited(i + 1, j, dir)
        elif dir == "r" and j + 1 < len(m[0]):
            mark_visited(i, j + 1, dir)
        elif dir == "l" and j > 0:
            mark_visited(i, j - 1, dir)
    elif m[i][j] == "|":
        if (dir == "u" or dir == "d") and any(
            [visited[d][i][j] for d in [dir, "l", "r"]]
        ):
            return
        if (dir == "l" or dir == "r") and (
            any([visited[d][i][j] for d in ["l", "r"]])
            or all([visited[d][i][j] for d in ["u", "d"]])
        ):
            return
        visited[dir][i][j] = True
        if dir != "d" and i > 0:
            mark_visited(i - 1, j, "u")
        if dir != "u" and i + 1 < len(m):
            mark_visited(i + 1, j, "d")
    elif m[i][j] == "-":
        if (dir == "l" or dir == "r") and any(
            [visited[d][i][j] for d in [dir, "u", "d"]]
        ):
            return
        if (dir == "u" or dir == "d") and (
            any([visited[d][i][j] for d in ["u", "d"]])
            or all([visited[d][i][j] for d in ["l", "r"]])
        ):
            return
        visited[dir][i][j] = True
        if dir != "l" and j + 1 < len(m[0]):
            mark_visited(i, j + 1, "r")
        if dir != "r" and j > 0:
            mark_visited(i, j - 1, "l")
    elif m[i][j] == "/":
        if visited[dir][i][j]:
            return
        visited[dir][i][j] = True
        if dir == "l" and i + 1 < len(m):
            mark_visited(i + 1, j, "d")
        elif dir == "r" and i > 0:
            mark_visited(i - 1, j, "u")
        elif dir == "u" and j + 1 < len(m[0]):
            mark_visited(i, j + 1, "r")
        elif dir == "d" and j > 0:
            mark_visited(i, j - 1, "l")
    elif m[i][j] == "\\":
        if visited[dir][i][j]:
            return
        visited[dir][i][j] = True
        if dir == "r" and i + 1 < len(m):
            mark_visited(i + 1, j, "d")
        elif dir == "l" and i > 0:
            mark_visited(i - 1, j, "u")
        elif dir == "d" and j + 1 < len(m[0]):
            mark_visited(i, j + 1, "r")
        elif dir == "u" and j > 0:
            mark_visited(i, j - 1, "l")


m = []
f = open("input", "r")
while True:
    line = f.readline()
    if not line:
        break
    m.append(line.rstrip())
f.close()
ec = 0
# start from top row
for _j in range(len(m[0])):
    visited = {
        "u": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "d": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "l": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "r": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
    }
    mark_visited(0, _j, "d")
    energized_count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if any([visited[d][i][j] for d in ["l", "r", "u", "d"]]):
                energized_count += 1
    ec = max(ec, energized_count)
# start from left row
for _i in range(len(m)):
    visited = {
        "u": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "d": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "l": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "r": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
    }
    mark_visited(_i, 0, "r")
    energized_count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if any([visited[d][i][j] for d in ["l", "r", "u", "d"]]):
                energized_count += 1
    ec = max(ec, energized_count)
# start from bottom row
for _j in range(len(m[0])):
    visited = {
        "u": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "d": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "l": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "r": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
    }
    mark_visited(len(m) - 1, _j, "u")
    energized_count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if any([visited[d][i][j] for d in ["l", "r", "u", "d"]]):
                energized_count += 1
    ec = max(ec, energized_count)
# start from right row
for _i in range(len(m)):
    visited = {
        "u": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "d": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "l": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
        "r": [[False for _ in range(len(m[0]))] for _ in range(len(m))],
    }
    mark_visited(_i, len(m[0]) - 1, "l")
    energized_count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if any([visited[d][i][j] for d in ["l", "r", "u", "d"]]):
                energized_count += 1
    ec = max(ec, energized_count)

print(ec)

