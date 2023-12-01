f = open('input', mode='r')
sum = 0
while True:
    line = f.readline()
    if not line:
        break
    digits_list = [int(char) for char in line if char.isdigit()]
    if len(digits_list) >= 1:
        sum += digits_list[0]*10 + digits_list[-1]
print(sum)
f.close()
