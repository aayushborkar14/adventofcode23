f = open("input", "r")
cur = []
ans = 0
lastdone = False
while True:
    if lastdone:
        break
    line = f.readline()
    if not line:
        lastdone = True
    line = line.rstrip()
    if not line:
        # process pattern here
        # look for vertical mirror
        n = len(cur[0])
        for i in range(n - 1):
            mirror = True
            for j in range(min(i + 1, n - i - 1)):
                s1 = "".join([s[i - j] for s in cur])
                s2 = "".join([s[i + j + 1] for s in cur])
                if s1 != s2:
                    mirror = False
                    break
            if mirror:
                ans += i + 1
        # look for horizontal mirror
        k = len(cur)
        for i in range(k - 1):
            mirror = True
            for j in range(min(i + 1, k - i - 1)):
                if cur[i - j] != cur[i + j + 1]:
                    mirror = False
                    break
            if mirror:
                ans += 100 * (i + 1)
        cur = []
        continue
    cur.append(line)
f.close()
print(ans)

