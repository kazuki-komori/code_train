import math


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


password = input()

status = [0, 0, 0]

for p in password:
    if p == "o":
        status[0] += 1
    if p == "?":
        status[1] += 1
    if p == "x":
        status[2] += 1

rest = 4 - status[0]
ans = 0

if rest < 0:
    print(0)
else:
    while True:
        print(status[1], rest)
        if rest == 0:
            ans += status[0] ** (4-status[0])
            break
        ans += comb(status[1], rest) * math.factorial(status[0]) * (status[0] ** (4 - rest - status[0]))
        rest -= 1

print(status)
print(ans)
# numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
