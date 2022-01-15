P = int(input())


def Factorial(n):
    if n == 1:
        return n
    else:
        return n * Factorial(n-1)


ans = 0

for i in range(10, 0, -1):
    if P / Factorial(i) >= 1:
        s = P // Factorial(i)
        if s > 100:
            P -= Factorial(i) * 100
            ans += 100
        else:
            P -= Factorial(i) * s
            ans += s

print(ans)
