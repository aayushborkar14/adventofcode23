f = open('input', 'r')
sum = 0
num_dict = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
while True:
    line = f.readline()
    if not line:
        break
    first_start = -1
    first_end = -1
    first_num = ''
    for num in num_dict.keys():
        index = line.find(num)
        if first_start == -1 and index != -1:
            first_start = index
            first_end = first_start + len(num) - 1
            first_num = num
        elif index != -1 and index < first_start:
            first_start = index
            first_end = first_start + len(num) - 1
            first_num = num
    line_rev = line[::-1]
    last_start = -1
    last_end = -1
    last_num = ''
    for num in num_dict.keys():
        index = line_rev.find(num[::-1])
        if last_start == -1 and index != -1:
            last_start = index
            last_end = last_start + len(num) - 1
            last_num = num
        elif index != -1 and index < last_start:
            last_start = index
            last_end = last_start + len(num) - 1
            last_num = num
    last_end_c = last_end
    last_end = len(line) - last_start - 1
    last_start = len(line) - last_end_c - 1
    if first_start != -1:
        if first_end != last_start:
            line = line[:first_start] + str(num_dict[first_num]) + line[first_start + len(first_num):]
            if first_start != last_start:
                last_start = last_start - (len(first_num) - 1)
                last_end = last_end - (len(first_num) - 1)
                line = line[:last_start] + str(num_dict[last_num]) + line[last_start + len(last_num):]
        else:
            num_before_first = False
            num_after_second = False
            for i in range(first_start):
                if line[i].isdigit():
                    num_before_first = True
                    break
            for i in range(last_end + 1, len(num)):
                if line[i].isdigit():
                    num_after_second = True
                    break
            if num_before_first and not num_after_second:
                line = line[:last_start] + str(num_dict[last_num]) + line[last_start + len(last_num):]
            elif num_after_second and not num_before_first:
                line = line[:first_start] + str(num_dict[first_num]) + line[first_start + len(first_num):]

    digits_list = [int(char) for char in line if char.isdigit()]
    if len(digits_list) >= 1:
        sum += digits_list[0]*10 + digits_list[-1]
print(sum)
f.close()
