ans = 0
f = open("input", "r")
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    spring = line.split()[0]
    springs = ""
    for i in range(5):
        springs += spring
        if i != 4:
            springs += "?"
    springs += "."
    nums = [int(x) for x in line.split()[1].split(",")] * 5
    n = len(springs)
    nums_len = len(nums)
    nums += [n + 1]
    dp = [
        [[0 for _ in range(n + 2)] for _ in range(nums_len + 2)] for _ in range(n + 1)
    ]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(nums_len + 1):
            for k in range(n + 1):
                cur = dp[i][j][k]
                if not cur:
                    continue
                if springs[i] == "." or springs[i] == "?":
                    if k == 0 or k == nums[j - 1]:
                        dp[i + 1][j][0] += cur
                if springs[i] == "#" or springs[i] == "?":
                    if k:
                        dp[i + 1][j][k + 1] += cur
                    else:
                        dp[i + 1][j + 1][k + 1] += cur
    ans += dp[n][nums_len][0]
f.close()
print(ans)

