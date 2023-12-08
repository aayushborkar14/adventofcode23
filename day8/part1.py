moves_str = ""
moves_dict = {}

f = open("input", "r")
moves_str = f.readline().rstrip()
f.readline()
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    key, values_str = line.split("=")
    key = key.strip()
    values_str = values_str.strip()[1:-1]
    values = tuple(value.strip() for value in values_str.split(","))
    moves_dict[key] = values
f.close()
pos = "AAA"
num_moves = 0
zfound = False
while True:
    for move in moves_str:
        num_moves += 1
        if move == "L":
            pos = moves_dict[pos][0]
        else:
            pos = moves_dict[pos][1]
        if pos == "ZZZ":
            zfound = True
            break
    if zfound:
        break
print(num_moves)

