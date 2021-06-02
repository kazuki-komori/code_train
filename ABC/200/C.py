import math

N = int(input())
A = list(map(int, input().split()))

ans = 0
s = [0]*200
for i in range(N):
    s[A[i]%200] += 1

print(s)
ans = 0
for i in range(200):
    ans += (s[i]*(s[i]-1)) // 2

print(ans)
