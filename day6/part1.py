from math import floor, ceil, pow, sqrt

f = open("input", "r")
t = int("".join([char for char in f.readline().rstrip() if char.isdigit()]))
d = int("".join([char for char in f.readline().rstrip() if char.isdigit()]))
f.close()
a = ceil((t - sqrt(pow(t, 2) - 4 * d)) / 2)
b = floor((t + sqrt(pow(t, 2) - 4 * d)) / 2)
ans = b - a + 1
print(ans)

