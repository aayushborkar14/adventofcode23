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
        ansfound = False
        for i in range(n - 1):
            num_differences = 0
            for j in range(min(i + 1, n - i - 1)):
                for s in cur:
                    if s[i - j] != s[i + j + 1]:
                        num_differences += 1
                    if num_differences > 1:
                        break
                if num_differences > 1:
                    break
            if num_differences == 1:
                ans += i + 1
                ansfound = True
                break
        if ansfound:
            cur = []
            continue
        # look for horizontal mirror
        k = len(cur)
        for i in range(k - 1):
            num_differences = 0
            for j in range(min(i + 1, k - i - 1)):
                for c in range(n):
                    if cur[i - j][c] != cur[i + j + 1][c]:
                        num_differences += 1
                    if num_differences > 1:
                        break
                if num_differences > 1:
                    break
            if num_differences == 1:
                ans += 100 * (i + 1)
                break
        cur = []
        continue
    cur.append(line)
f.close()
print(ans)

