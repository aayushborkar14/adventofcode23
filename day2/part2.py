import re


def extract_tuples(statement):
    # Define a regular expression pattern to match tuples
    pattern = r"(\d+)\s*([a-zA-Z]+)"

    # Find all matches using the pattern
    matches = re.findall(pattern, statement)

    # Convert matches to a list of tuples
    tuples_list = [(int(count), color.lower()) for count, color in matches]

    return tuples_list


powers = []
f = open("input", "r")
while True:
    line = f.readline()
    if not line:
        break
    tlist = extract_tuples(line)
    maxstore = {"red": 0, "green": 0, "blue": 0}
    for t in tlist:
        if t[0] > maxstore[t[1]]:
            maxstore[t[1]] = t[0]
    power = maxstore["red"] * maxstore["green"] * maxstore["blue"]
    powers.append(power)
print(sum(powers))
f.close()

