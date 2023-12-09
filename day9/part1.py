ans = 0
f = open("input", "r")
while True:
    line = f.readline()
    if not line:
        break
    nums = [int(num) for num in line.rstrip().split()]
    diff = [nums]
    while True:
        next_diff = []
        for i in range(1, len(diff[-1])):
            next_diff.append(diff[-1][i] - diff[-1][i - 1])
        diff.append(next_diff)
        if all(num == 0 for num in next_diff):
            break
    diff[-1].append(0)
    for i in range(len(diff) - 2, -1, -1):
        diff[i].append(diff[i][-1] + diff[i + 1][-1])
    ans += diff[0][-1]
f.close()
print(ans)

