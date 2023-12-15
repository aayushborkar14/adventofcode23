def hash(s):
    hash_val = 0
    for c in s:
        hash_val += ord(c)
        hash_val *= 17
        hash_val %= 256
    return hash_val


f = open("input", "r")
line = f.readline().rstrip()
f.close()
value = 0
for s in line.split(","):
    value += hash(s)
print(value)

