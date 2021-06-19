N = int(input())

ans = 0
i = 1
box = 0

while True:
    if box >= N:
        print(ans)
        break
    box += i
    i += 1
    ans += 1
