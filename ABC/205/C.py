A, B, C = map(int, input().split())


def pow_k(x, n):
    ans = 1
    b = bin(n)[::2]
    for i in range(len(b)):
        if (n >> i) & 1:
            ans *= x
        x *= x
    return ans


ac = pow_k(A, C)
bc = pow_k(B, C)

if ac < bc:
    print("<")
elif ac > bc:
    print(">")
else:
    print("=")
