N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

point = 0

for idx, a in enumerate(A):
    point += B[a-1]
    if idx != N-1:
        if A[idx + 1] - A[idx] == 1:
            point += C[a-1]

print(point)
