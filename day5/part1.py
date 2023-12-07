def mapper(n, dict):
    """
    Function that maps n to a range of values in dict, and returns n itself if n is not found in any range
    """
    for a, b in dict.keys():
        if n >= a and n <= b:
            return n + dict[(a, b)]
    return n


seed_raw = []
soils = {}
ferts = {}
waters = {}
lights = {}
temps = {}
humids = {}
locs = {}

f = open("input", "r")
pres = ""
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    if line.startswith("seeds:"):
        pres = "s"
        seed_raw = [int(num) for num in line.split() if num.isdigit()]
        continue
    elif "map:" in line:
        continue
    elif pres == "s":
        pres = "ss"
        continue
    elif pres == "ss":
        if not line:
            pres = "sf"
            continue
        num_list = [int(num) for num in line.split()]
        soils[(num_list[1], num_list[1] + num_list[2] - 1)] = num_list[0] - num_list[1]
    elif pres == "sf":
        if not line:
            pres = "fw"
            continue
        num_list = [int(num) for num in line.split()]
        ferts[(num_list[1], num_list[1] + num_list[2] - 1)] = num_list[0] - num_list[1]
    elif pres == "fw":
        if not line:
            pres = "wl"
            continue
        num_list = [int(num) for num in line.split()]
        waters[(num_list[1], num_list[1] + num_list[2] - 1)] = num_list[0] - num_list[1]
    elif pres == "wl":
        if not line:
            pres = "lt"
            continue
        num_list = [int(num) for num in line.split()]
        lights[(num_list[1], num_list[1] + num_list[2] - 1)] = num_list[0] - num_list[1]
    elif pres == "lt":
        if not line:
            pres = "th"
            continue
        num_list = [int(num) for num in line.split()]
        temps[(num_list[1], num_list[1] + num_list[2] - 1)] = num_list[0] - num_list[1]
    elif pres == "th":
        if not line:
            pres = "hl"
            continue
        num_list = [int(num) for num in line.split()]
        humids[(num_list[1], num_list[1] + num_list[2] - 1)] = num_list[0] - num_list[1]
    elif pres == "hl":
        num_list = [int(num) for num in line.split()]
        locs[(num_list[1], num_list[1] + num_list[2] - 1)] = num_list[0] - num_list[1]
f.close()
ans = 0.1
for seed in seed_raw:
    loc = mapper(
        mapper(
            mapper(
                mapper(mapper(mapper(mapper(seed, soils), ferts), waters), lights),
                temps,
            ),
            humids,
        ),
        locs,
    )
    if ans == 0.1:
        ans = loc
    else:
        ans = min(ans, loc)
print(ans)

