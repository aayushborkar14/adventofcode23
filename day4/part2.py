f = open("input", "r")

lists_before = []
lists_after = []
while True:
    line = f.readline()
    if not line:
        break
    # Find the index of ": "
    index_colon_space = line.index(": ")

    # Extract the substring after ": "
    input_string = line[index_colon_space + 2 :]

    # Split the string into two parts using the "|"
    before_pipe, after_pipe = input_string.split("|")

    # Convert the strings to lists of integers
    list_before_pipe = [int(num) for num in before_pipe.split()]
    list_after_pipe = [int(num) for num in after_pipe.split()]

    lists_before.append(list_before_pipe)
    lists_after.append(list_after_pipe)

count = [1] * 188
for i in range(188):
    num = 0
    for a in lists_after[i]:
        if a in lists_before[i]:
            num += 1
    for j in range(i + 1, i + 1 + num):
        count[j] += count[i]
print(sum(count))
f.close()

