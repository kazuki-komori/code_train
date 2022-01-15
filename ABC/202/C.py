N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0

A_dict = {}

for a in A:
    if str(a) not in A_dict.keys():
        A_dict[str(a)] = 0
    A_dict[str(a)] += 1

for c in C:
    if str(B[c-1]) in A_dict.keys():
        ans += A_dict[str(B[c-1])]

print(ans)
