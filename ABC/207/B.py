A, B, C, D = map(int, input().split())

LB = A
R = 0
ans = 0

while True:
    if LB <= R * D:
        print(ans)
        break
    ans += 1
    LB += B
    R += C
    if R * D < LB:
        if C * D <= B:
            print(-1)
            exit()
