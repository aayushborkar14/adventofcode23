import queue

FILENAME = "input"
output = {}
modtype = {}
ffstate = {}
constate = {}
f = open(FILENAME, "r")
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    modname = line.split(" -> ")[0][1:]
    if line.startswith("%"):
        modtype[modname] = "%"
        ffstate[modname] = False
    elif line.startswith("&"):
        modtype[modname] = "&"
        constate[modname] = {}
f.close()
f = open(FILENAME, "r")
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    lhs, rhs = line.split(" -> ")[0], line.split(" -> ")[1]
    if lhs.startswith("%") or lhs.startswith("&"):
        output[lhs[1:]] = [mod for mod in rhs.split(", ")]
        for mod in rhs.split(", "):
            if mod in modtype.keys():
                if modtype[mod] == "&":
                    constate[mod][lhs[1:]] = False
            else:
                modtype[mod] = "out"
    else:
        output[lhs] = [mod for mod in rhs.split(", ")]
f.close()
highs = []
lows = []
while True:
    high_c, low_c = 0, 1
    q = queue.Queue()
    for mod in output["broadcaster"]:
        q.put((mod, False, "b"))
    while not q.empty():
        v, high, u = q.get()
        if high:
            high_c += 1
        else:
            low_c += 1
        if modtype[v] == "%":
            if not high:
                ffstate[v] = not ffstate[v]
                for omod in output[v]:
                    q.put((omod, ffstate[v], v))
        elif modtype[v] == "&":
            signal = True
            constate[v][u] = high
            if all(constate[v].values()):
                signal = False
            for omod in output[v]:
                q.put((omod, signal, v))
    highs.append(high_c)
    lows.append(low_c)
    if len(highs) == 1000:
        break
ans = sum(lows) * sum(highs)
print(ans)
