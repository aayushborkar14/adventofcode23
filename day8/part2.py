from math import gcd

moves_str = ""
moves_dict = {}
end_with_A = []

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
    if key.endswith("A"):
        end_with_A.append(key)
f.close()
num_moves_list = [0] * len(end_with_A)
for idx, start in enumerate(end_with_A):
    pos = start
    num_moves = 0
    zfound = False
    while True:
        for move in moves_str:
            num_moves += 1
            if move == "L":
                pos = moves_dict[pos][0]
            else:
                pos = moves_dict[pos][1]
            if pos.endswith("Z"):
                zfound = True
                num_moves_final = num_moves
        if zfound:
            break
    num_moves_list[idx] = num_moves
lcm = 1
for i in num_moves_list:
    lcm = lcm * i // gcd(lcm, i)
# LCM solutions works because the input is crafted in such a way
print(lcm)

