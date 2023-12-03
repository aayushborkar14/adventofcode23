import re

with open("input", "r") as f:
    lines = [line.rstrip() for line in f]
sum = 0
chars = ["*", "/", "\\", "!", "@", "#", "$", "%", "^", "&", "+", "=", "-"]

for i in range(len(lines)):
    line = lines[i]
    matches = re.finditer(r"\d+", line)
    for match in matches:
        aster = False
        nexti = match.start() + len(match.group())
        # look in same line
        if match.start() and (line[match.start() - 1] in chars):
            aster = True
        elif (nexti < len(lines)) and (line[nexti] in chars):
            aster = True
        # look down and up
        if i < len(lines) - 1:
            for j in range(match.start(), nexti):
                if lines[i + 1][j] in chars:
                    aster = True
                    break
        if i > 0:
            for j in range(match.start(), nexti):
                if lines[i - 1][j] in chars:
                    aster = True
                    break
        # look diagonally
        if (
            i < len(lines) - 1
            and match.start()
            and match.start() - 1 < len(lines[i + 1])
            and lines[i + 1][match.start() - 1] in chars
        ):
            aster = True
        elif (
            i < len(lines) - 1
            and nexti < len(lines[i + 1])
            and lines[i + 1][nexti] in chars
        ):
            aster = True
        elif (
            i > 0
            and match.start()
            and match.start() - 1 < len(lines[i - 1])
            and lines[i - 1][match.start() - 1] in chars
        ):
            aster = True
        elif i > 0 and nexti < len(lines[i - 1]) and lines[i - 1][nexti] in chars:
            aster = True

        if aster:
            sum += int(match.group())
print(sum)

