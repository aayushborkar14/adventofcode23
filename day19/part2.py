def intersect(a, b):
    if a[0] <= b[0] and b[0] <= a[1] and a[1] <= b[1]:
        return (b[0], a[1])
    if a[0] >= b[0] and a[1] <= b[1]:
        return (a[0], a[1])
    if b[0] >= a[0] and b[1] <= a[1]:
        return (b[0], b[1])
    if b[0] <= a[0] and a[0] <= b[1] and b[1] <= a[1]:
        return (a[0], b[1])
    return (-1, -1)


FILENAME = "input"

wfs = {}
f = open(FILENAME, "r")
wfdone = False
ans = 0
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    if not line:
        break
    wfname = line.split("{")[0]
    wf_contents = {}
    wf_last = ""
    for part_details in line.split("{")[1][:-1].split(","):
        if part_details.find(":") != -1:
            wf_contents[part_details.split(":")[0]] = part_details.split(":")[1]
        else:
            wf_last = part_details
    wfs[wfname] = (wf_contents, wf_last)
f.close()
with open(FILENAME, "r") as file:
    lines_with_A = [line.rstrip() for line in file if "A" in line]
for line in lines_with_A:
    while "A" in line:
        ranges = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
        pres = "A"
        prev = line.split("{")[0]
        null_sect = False
        in_reached = False
        while True:
            pres_found = False
            for pd in wfs[prev][0].keys():
                if wfs[prev][0][pd] == pres:
                    pres_found = True
                    if ">" in pd:
                        ranges[pd.split(">")[0]] = intersect(
                            ranges[pd.split(">")[0]], (int(pd.split(">")[1]) + 1, 4000)
                        )
                        if ranges[pd.split(">")[0]] == (-1, -1):
                            null_sect = True
                    else:
                        ranges[pd.split("<")[0]] = intersect(
                            ranges[pd.split("<")[0]], (1, int(pd.split("<")[1]) - 1)
                        )
                        if ranges[pd.split("<")[0]] == (-1, -1):
                            null_sect = True
                    break
                if ">" in pd:
                    ranges[pd.split(">")[0]] = intersect(
                        ranges[pd.split(">")[0]], (1, int(pd.split(">")[1]))
                    )
                    if ranges[pd.split(">")[0]] == (-1, -1):
                        null_sect = True
                        break
                else:
                    ranges[pd.split("<")[0]] = intersect(
                        ranges[pd.split("<")[0]], (int(pd.split("<")[1]), 4000)
                    )
                    if ranges[pd.split("<")[0]] == (-1, -1):
                        null_sect = True
                        break
            if null_sect:
                break
            if not pres_found and wfs[prev][1] == pres:
                pres_found = True
            if not pres_found:
                break
            if prev == "in":
                in_reached = True
                break
            with open(FILENAME, "r") as f:
                lines_with_prev1 = [
                    linep.rstrip() for linep in f if (":" + prev + ",") in linep
                ]
            with open(FILENAME, "r") as f:
                lines_with_prev2 = [
                    linep.rstrip() for linep in f if ("," + prev + "}") in linep
                ]
            pres = prev
            for linep in lines_with_prev1 + lines_with_prev2:
                if linep.split("{")[0] != prev:
                    prev = linep.split("{")[0]
                    break
        line = line.replace("A", "P", 1)
        wfname = line.split("{")[0]
        a_found = False
        dictc = wfs[wfname][0]
        for pdkey in dictc.keys():
            if dictc[pdkey] == "A":
                a_found = True
                dictc[pdkey] = "P"
                wfs[wfname] = (dictc, wfs[wfname][1])
                break
        if not a_found:
            if wfs[wfname][1] == "A":
                wfs[wfname] = (dictc, "P")
        if null_sect:
            continue
        if in_reached:
            tans = 1
            for rval in ranges.values():
                tans *= rval[1] - rval[0] + 1
            print(tans)
            ans += tans
print(ans)

