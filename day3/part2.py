with open("input", "r") as f:
    lines = [line.rstrip() for line in f]
sum = 0
for i in range(len(lines)):
    line = lines[i]
    asterisk_indices = [j for j, char in enumerate(line) if char == "*"]
    for ast in asterisk_indices:
        nums = []
        # check in same line
        if ast > 0 and line[ast - 1].isdigit():
            num = line[ast - 1]
            j = ast - 2
            while j >= 0 and line[j].isdigit():
                num = line[j] + num
                j -= 1
            nums.append(int(num))
        if ast + 1 < len(line) and line[ast + 1].isdigit():
            num = line[ast + 1]
            j = ast + 2
            while j < len(line) and line[j].isdigit():
                num += line[j]
                j += 1
            nums.append(int(num))
        # check up and down
        upfound = False
        downfound = False
        if ast < len(lines[i - 1]) and lines[i - 1][ast].isdigit():
            upfound = True
            num = lines[i - 1][ast]
            j = ast - 1
            while j >= 0 and lines[i - 1][j].isdigit():
                num = lines[i - 1][j] + num
                j -= 1
            j = ast + 1
            while j <= len(lines[i - 1]) and lines[i - 1][j].isdigit():
                num += lines[i - 1][j]
                j += 1
            nums.append(int(num))
        if ast < len(lines[i + 1]) and lines[i + 1][ast].isdigit():
            downfound = True
            num = lines[i + 1][ast]
            j = ast - 1
            while j >= 0 and lines[i + 1][j].isdigit():
                num = lines[i + 1][j] + num
                j -= 1
            j = ast + 1
            while j <= len(lines[i + 1]) and lines[i + 1][j].isdigit():
                num += lines[i + 1][j]
                j += 1
            nums.append(int(num))

        # check diagonally
        if (
            not upfound
            and i
            and ast > 0
            and ast - 1 < len(lines[i - 1])
            and lines[i - 1][ast - 1].isdigit()
        ):
            num = lines[i - 1][ast - 1]
            j = ast - 2
            while j >= 0 and lines[i - 1][j].isdigit():
                num = lines[i - 1][j] + num
                j -= 1
            nums.append(int(num))
        if (
            not downfound
            and i + 1 < len(lines)
            and ast > 0
            and ast - 1 < len(lines[i + 1])
            and lines[i + 1][ast - 1].isdigit()
        ):
            num = lines[i + 1][ast - 1]
            j = ast - 2
            while j >= 0 and lines[i + 1][j].isdigit():
                num = lines[i + 1][j] + num
                j -= 1
            nums.append(int(num))
        if (
            not upfound
            and i
            and ast + 1 < len(lines[i - 1])
            and lines[i - 1][ast + 1].isdigit()
        ):
            num = lines[i - 1][ast + 1]
            j = ast + 2
            while j < len(lines[i - 1]) and lines[i - 1][j].isdigit():
                num += lines[i - 1][j]
                j += 1
            nums.append(int(num))
        if (
            not downfound
            and i + 1 < len(lines)
            and ast + 1 < len(lines[i + 1])
            and lines[i + 1][ast + 1].isdigit()
        ):
            num = lines[i + 1][ast + 1]
            j = ast + 2
            while j < len(lines[i + 1]) and lines[i + 1][j].isdigit():
                num += lines[i + 1][j]
                j += 1
            nums.append(int(num))

        if len(nums) == 2:
            sum += nums[0] * nums[1]
print(sum)

