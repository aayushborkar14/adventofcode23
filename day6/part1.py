from math import floor, ceil, pow, sqrt

f = open("input", "r")
times = [int(num) for num in f.readline().rstrip().split() if num.isdigit()]
distances = [int(num) for num in f.readline().rstrip().split() if num.isdigit()]
f.close()
ans = 1
for idx, (t, d) in enumerate(zip(times, distances)):
    if pow(t, 2) < 4 * d:
        ans *= 0
        break
    a = ceil((t - sqrt(pow(t, 2) - 4 * d)) / 2)
    b = floor((t + sqrt(pow(t, 2) - 4 * d)) / 2)
    ans *= b - a + 1
print(ans)

