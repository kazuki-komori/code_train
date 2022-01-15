N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

ans += K // N
K -= N * ans

b = list.copy(a)
b.sort()

k = b[K]

for val in a:
    if val < k:
        print(ans + 1)
    else:
        print(ans)
