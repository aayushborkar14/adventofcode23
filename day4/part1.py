f = open("input", "r")
sum = 0
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

    common_matches = 0
    for num in list_after_pipe:
        if num in list_before_pipe:
            common_matches += 1
    sum += int(2 ** (common_matches - 1))
print(sum)
f.close()

