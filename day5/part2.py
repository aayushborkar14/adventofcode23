def mapper(n, tdict):
    """
    Function that maps n to an increment in dict, and returns 0 if n is not found in any range
    """
    for a, b in tdict.keys():
        if n >= a and n <= b:
            return tdict[(a, b)]
    return 0


def rec(l, r, i):
    tdict = {}
    next = ""
    if i == "seed":
        tdict = soils
        next = "soil"
    elif i == "soil":
        tdict = ferts
        next = "fert"
    elif i == "fert":
        tdict = waters
        next = "water"
    elif i == "water":
        tdict = lights
        next = "light"
    elif i == "light":
        tdict = temps
        next = "temp"
    elif i == "temp":
        tdict = humids
        next = "humid"
    elif i == "humid":
        tdict = locs
        next = "loc"
    elif i == "loc":
        return l
    if l == r:
        inc = mapper(l, tdict)
        return rec(l + inc, r + inc, next)
    plocs = []
    proceseed_ranges = []
    for a, b in tdict.keys():
        intersects = False
        ld = 0
        rd = 0
        if l <= a and r <= b and r >= a:
            intersects = True
            ld = a
            rd = r
        elif l >= a and r >= b and l <= b:
            intersects = True
            ld = l
            rd = b
        elif l >= a and r <= b:
            intersects = True
            ld = l
            rd = r
        elif l <= a and r >= b:
            intersects = True
            ld = a
            rd = b
        if intersects:
            proceseed_ranges.append((ld, rd))
            inc = mapper(ld, tdict)
            plocs.append(rec(ld + inc, rd + inc, next))
    proceseed_ranges = sorted(proceseed_ranges)
    if not len(proceseed_ranges):
        plocs.append(rec(l, r, next))
    for j in range(len(proceseed_ranges)):
        a = proceseed_ranges[j][0]
        b = proceseed_ranges[j][1]
        if i == 0:
            if l < a:
                plocs.append(rec(l, a - 1, next))
        else:
            aprev = proceseed_ranges[j - 1][0]
            bprev = proceseed_ranges[j - 1][0]
            if bprev + 1 < aprev:
                plocs.append(rec(bprev + 1, a - 1, next))
            if i == len(proceseed_ranges) - 1 and b < r:
                plocs.append(rec(b + 1, r, next))
    return min(plocs)


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
flocs = []
seeds = [(seed_raw[i], seed_raw[i + 1]) for i in range(0, len(seed_raw), 2)]
for a, b in seeds:
    flocs.append(rec(a, b + a - 1, "seed"))
print(min(flocs))

