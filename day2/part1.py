import re

def extract_tuples(statement):
    # Define a regular expression pattern to match tuples
    pattern = r'(\d+)\s*([a-zA-Z]+)'
    
    # Find all matches using the pattern
    matches = re.findall(pattern, statement)
    
    # Convert matches to a list of tuples
    tuples_list = [(int(count), color.lower()) for count, color in matches]
    
    return tuples_list

possible = []
f = open('input', 'r')
while True:
    line = f.readline()
    if not line:
        break
    match = re.search(r"Game (\d+):", line)
    id = 0
    if match:
        id = match.group(1)
    qualifies = True
    tlist = extract_tuples(line)
    maxstore = {'red': 12, 'green': 13, 'blue': 14}
    for t in tlist:
        if t[0] > maxstore[t[1]]:
            qualifies = False
            break
    if qualifies:
        possible.append(int(id))
print(sum(possible))
f.close()

