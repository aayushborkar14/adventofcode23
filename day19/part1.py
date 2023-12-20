wfs = {}
f = open("input", "r")
wfdone = False
ans = 0
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    if not line:
        wfdone = True
        continue
    if wfdone:
        xmas = {
            key_value.split("=")[0]: int(key_value.split("=")[1])
            for key_value in line.strip("{}").split(",")
        }
        next = "in"
        while next not in ("A", "R"):
            wfc, wfl = wfs[next]
            nextfound = False
            for pd in wfc.keys():
                if pd.find(">") != -1 and xmas[pd.split(">")[0]] > int(
                    pd.split(">")[1]
                ):
                    next = wfc[pd]
                    nextfound = True
                    break
                elif pd.find("<") != -1 and xmas[pd.split("<")[0]] < int(
                    pd.split("<")[1]
                ):
                    next = wfc[pd]
                    nextfound = True
                    break
            if not nextfound:
                next = wfl
        if next == "A":
            ans += sum(xmas.values())

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
print(ans)

