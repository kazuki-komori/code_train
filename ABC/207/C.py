N = int(input())
data = [list(map(int, input().split()))for _ in range(N)]

T = []

for d in data:
    if d[0] == 1:
        T.append([d[1], d[2]])
    if d[0] == 2:
        T.append([d[1], d[2] - 0.5])
    if d[0] == 3:
        T.append([d[1] + 0.5, d[2]])
    if d[0] == 4:
        T.append([d[1] + 0.5, d[2] - 0.5])

ans = 0

for (idx, t1) in enumerate(T):
    for t2 in T[idx + 1:]:
        if t2[0] <= t1[0] <= t2[1]:
            ans += 1
            continue
        if t2[0] <= t1[1] <= t2[1]:
            ans += 1
            continue
        if t1[0] <= t2[0] <= t1[1]:
            ans += 1
            continue
        if t1[0] <= t2[1] <= t1[1]:
            ans += 1
            continue

print(ans)
