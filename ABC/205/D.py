N, Q = map(int, input().split())

A = list(map(int, input().split()))
K = [int(input()) for _ in range(Q)]

pass_arr = []


def check(n):
    d2 = 0
    while True:
        d = sum(map(lambda i:i <= n, A))
        if n > 20:
            break
        if d == d2:
            return n
        else:
            n += d
            n -= d2
            d2 = d


for k in K:
    print(check(k))
