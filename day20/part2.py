import queue
from math import lcm

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
rxparent = ""
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    lhs, rhs = line.split(" -> ")[0], line.split(" -> ")[1]
    if lhs.startswith("%") or lhs.startswith("&"):
        output[lhs[1:]] = [mod for mod in rhs.split(", ")]
        for mod in rhs.split(", "):
            if mod == "rx":
                rxparent = lhs[1:]
            if mod in modtype.keys():
                if modtype[mod] == "&":
                    constate[mod][lhs[1:]] = False
            else:
                modtype[mod] = "out"
    else:
        output[lhs] = [mod for mod in rhs.split(", ")]
f.close()
periods = []
# input has been crafted in such a way that rxparent is of '&' type and has 4 parents,
# each of which run in an independent cycle, i.e., the 4 cycles are connected only via broadcaster
# so, it suffices to find the lcm of the period of each of the 4 cycles
for pmod in constate[rxparent].keys():
    press = 0
    numhigh = 0
    first = -1
    second = -1
    while True:
        press += 1
        q = queue.Queue()
        for mod in output["broadcaster"]:
            q.put((mod, False, "b"))
        while not q.empty():
            v, high, u = q.get()
            if v == pmod and not high:
                numhigh += 1
                if first == -1:
                    first = press
                else:
                    second = press
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
        if numhigh >= 2:
            break
    periods.append(second - first)
ans = lcm(*periods)
print(ans)

