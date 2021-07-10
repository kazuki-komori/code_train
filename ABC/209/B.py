N, X = map(int, input().split())
A = list(map(int, input().split()))

price = 0

for i, a in enumerate(A):
    if (i + 1) % 2 == 0:
        price += a - 1
    else:
        price += a

if price <= X:
    print("Yes")
else:
    print("No")
