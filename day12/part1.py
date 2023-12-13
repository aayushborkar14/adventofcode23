def perms(s, nums):
    for i, c in enumerate(s):
        if c == "?":
            return perms(s[:i] + "." + s[i + 1 :], nums) + perms(
                s[:i] + "#" + s[i + 1 :], nums
            )
    loc_nums = []
    prev_hash = False
    pres_hash_len = 0
    for c in s:
        if c == "#":
            prev_hash = True
            pres_hash_len += 1
        elif prev_hash:
            prev_hash = False
            loc_nums.append(pres_hash_len)
            pres_hash_len = 0
    if s[len(s) - 1] == "#":
        loc_nums.append(pres_hash_len)
    if nums == loc_nums:
        return 1
    return 0


ans = 0
f = open("input", "r")
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip()
    springs = line.split()[0]
    nums = [int(x) for x in line.split()[1].split(",")]
    ans += perms(springs, nums)
f.close()
print(ans)

