N = int(input())

ans = 0

while True:
    res = 2 ** ans
    if res > N:
        print(ans -1)
        exit()
    ans += 1

