N, K = map(int, input().split())

for _ in range(K):
    if int(N) % 200 == 0:
        N = int(int(N) / 200)
    else:
        N = str(N) + "200"

print(N)