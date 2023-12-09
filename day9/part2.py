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
    for i in range(len(diff) - 2, -1, -1):
        diff[i].insert(0, diff[i][0] - diff[i + 1][0])
    ans += diff[0][0]
f.close()
print(ans)

