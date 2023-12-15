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
focusing_power = 0
boxes = [[] for _ in range(256)]
fl = {}
for s in line.split(","):
    split_char = "-" if ("-" in s) else "="
    label = s.split(split_char)[0]
    boxno = hash(label)
    sfl = s.split(split_char)[1]
    if "-" in s and label in boxes[boxno]:
        boxes[boxno].remove(label)
    elif "=" in s and label in boxes[boxno]:
        fl[label] = int(sfl)
    elif "=" in s:
        boxes[boxno].append(label)
        fl[label] = int(sfl)
for boxno, box in enumerate(boxes):
    for slotno, label in enumerate(box):
        focusing_power += (boxno + 1) * (slotno + 1) * fl[label]
print(focusing_power)

