N = int(input())
A = list(map(int, input().split()))

A.sort()
permit = list(range(1, max(A) + 1))

print("Yes" if permit == A else "No")
