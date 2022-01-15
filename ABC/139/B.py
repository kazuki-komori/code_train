import math

A, B = map(int, input().split())

ans = ((B - A) / (A - 1))

print(math.ceil(ans + 1))
