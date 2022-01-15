N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for idx in range(N):
    score = 0
    for idx2 in range(M):
        score += A[idx][idx2] * B[idx2]
    score += C
    if score > 0:
        ans += 1

print(ans)
